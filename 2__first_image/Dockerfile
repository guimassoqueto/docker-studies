FROM node:16.17-alpine3.15

WORKDIR /app

ENV PORT=8000

COPY . .

RUN yarn install && yarn run tsc

EXPOSE ${PORT}

ENTRYPOINT [ "yarn", "start" ]
