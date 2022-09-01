FROM node:18-alpine3.15

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . .

ENV PORT 80

EXPOSE $PORT

# VOLUME [ "/app/feedback" ]
# anonymous volumes: define which files / folders you want to persist even after the container is removed

CMD ["npm", "run", "start"]