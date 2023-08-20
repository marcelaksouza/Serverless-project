FROM node:alpine

# Here we define '/app' as base directory.
WORKDIR /client

# file from host to /app folder in the container
COPY package.json /client

RUN yarn install

COPY . /client

CMD ["yarn", "run", "start"]

