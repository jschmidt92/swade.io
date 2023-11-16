FROM python:3.11-alpine

WORKDIR /app

# VOLUME /swadeIOAPI

RUN apk add --update --no-cache bash gcc libffi-dev musl-dev openssl-dev postgresql-dev

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# CMD ["python3", "manage.py runserver 0.0.0.0:4000"]

STOPSIGNAL SIGINT
