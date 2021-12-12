FROM node:lts-alpine

RUN apk update

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . ./

RUN npm run build
