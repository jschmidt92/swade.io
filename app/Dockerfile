FROM node:alpine

WORKDIR /app

# VOLUME /swadeIOApp

RUN apk add --update --no-cache bash gcc libffi-dev musl-dev openssl-dev

COPY package*.json ./

RUN npm i

COPY . /app

# CMD ["npm", "run", "dev"]

STOPSIGNAL SIGINT
