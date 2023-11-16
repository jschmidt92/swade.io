FROM python:3.11-alpine

WORKDIR /app

# VOLUME /swadeIOBot

RUN apk add --update --no-cache bash ffmpeg gcc libffi-dev musl-dev openssl-dev

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# CMD ["python3", "main.py"]

STOPSIGNAL SIGINT
