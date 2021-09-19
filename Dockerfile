FROM python3.8.3-slim-buster

COPY . /src

RUN pip install -r /src/requirements.txt
