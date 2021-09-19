FROM python:3.8-slim-buster

RUN adduser --quiet worker
USER worker
WORKDIR /home/worker
COPY . /home/worker

RUN pip install -r /home/worker/requirements.txt

ENTRYPOINT python3.8 /home/worker/server.py
