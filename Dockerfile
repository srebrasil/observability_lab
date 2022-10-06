FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . .
RUN pip3 install -r requirements.txt