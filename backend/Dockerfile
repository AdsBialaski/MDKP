FROM alpine:latest

WORKDIR /app
RUN apk add --no-cache python3 py3-pip

COPY requirements.txt /app/

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY . .
ENTRYPOINT ["python3", "main.py"]
