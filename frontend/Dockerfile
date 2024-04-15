FROM alpine:latest

WORKDIR /app
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update && apk add --no-cache nodejs npm

COPY package.json ./
RUN npm install --silent

COPY . .
ENTRYPOINT ["npm", "run", "dev", "--", "--host"]

