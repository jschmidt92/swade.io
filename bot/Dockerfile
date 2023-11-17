# FROM python:3.11-alpine
FROM ubuntu

WORKDIR /app

# VOLUME /swadeIOBot

# RUN apk add --update --no-cache bash ffmpeg gcc libffi-dev musl-dev openssl-dev python3 py3-pip

RUN apt-get update && apt-get install -y ffmpeg python3 python3-pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python3", "main.py"]

STOPSIGNAL SIGINT
