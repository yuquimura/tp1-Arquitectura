FROM node:10
RUN mkdir /app
WORKDIR /app
COPY app.js package.json package-lock.json ./
RUN npm i
EXPOSE 3000
CMD [ "node", "app.js" ]
