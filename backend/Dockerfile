FROM alpine:latest

WORKDIR /app
RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /app/

COPY . .
ENTRYPOINT ["python3", "main.py"]
