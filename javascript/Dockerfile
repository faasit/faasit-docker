FROM node:18


RUN mkdir -p /app
RUN cd /app && npm install express
COPY ./nodejs14/src/server.js /app/app.js
RUN mkdir -p /node_modules
COPY faasit-runtime /node_modules/faasit-runtime
RUN npm install -g /node_modules/faasit-runtime
RUN npm install -g pnpm --registry=https://registry.npmmirror.com/

WORKDIR /code

ENV FAASIT_PROVIDER=local-once
