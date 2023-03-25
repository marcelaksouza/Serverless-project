# Base image
FROM node:12.16.1

# Label docker image
LABEL type "dynamoDB-container"

WORKDIR /app

RUN npm install -g dynamodb-admin

CMD ["dynamodb-admin"]