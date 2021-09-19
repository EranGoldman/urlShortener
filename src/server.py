#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, redirect, render_template
from flask_restful import Resource, Api
import redis
import random
import string
import hashlib
import base64

app = Flask(__name__)
api = Api(app, "/api/v1")

REDIS_SERVER = 'localhost'

class Shorten(Resource):
    def post(self, url):
        """Shorten the string url
        This function use md5[:6] for randomizing the hash and avoid collisions
        as shown in the collision test file in tools dir

        Example of use : 
        curl -X POST <server ip>/api/v1/shorten/<url in url encode string>
        """
        r = redis.Redis(host=REDIS_SERVER, port=6379, db=0)
        if r.get(url) : 
            return {'exist':str(r.get(url))},200
        hashed = hashlib.md5(url.encode("utf-8")).hexdigest().encode('ascii')
        encoded = base64.b64encode(hashed)[:6].decode("utf-8")
        # this loop will happen once every really alot
        while r.get(hashed):
          url= url+ ''.join(random.choice(string.ascii_lowercase) for i in range(4)) # add random salt of 4 lettera at the end of the url

        r.set(encoded,url)
        r.set(url,encoded)
        return {'shorten':encoded},200


class Lookup(Resource):
    def post(self,id):
        """Look up for the identifier in the db
        """
        r = redis.Redis(REDIS_SERVER, port=6379, db=0)
        return {'url':str(r.get(id))},200

api.add_resource(Shorten, '/shorten/<string:url>')
api.add_resource(Lookup, '/lookup/<string:id>')

@app.route('/')
def index():
  return json.dumps({'name': 'alice',
    'email': 'alice@outlook.com'})
 
 
@app.route('/<id>',methods=['GET'])
def redirecter(id):
    r = redis.Redis(host=REDIS_SERVER, port=6379, db=0)
    unshort = r.get(id)
    if unshort:
        return render_template("redirect.html",url=unshort),200
    return render_template("404.html"), 404


@app.errorhandler(404)
def not_found(e):
  if request.path.endswith("/") and request.path[:-1] in all_endpoints:
    return redirect(request.path[:-1]), 302
  return render_template("404.html"), 404

app.run(debug = True)
