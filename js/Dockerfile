FROM node:10FROM
RUN mkdir /apt/app
WORKDIR /apt/app
COPY app.js package.json package-lock.json ./
RUN npm i
ENTRYPOINT ['node','app.js']