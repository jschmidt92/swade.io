FROM node:alpine

WORKDIR /app

# VOLUME /swadeIOPeer

RUN apk add --update --no-cache bash gcc libffi-dev musl-dev openssl-dev

COPY package*.json ./

RUN npm i

COPY . /app

CMD ["npm", "run", "build"]

STOPSIGNAL SIGINT
