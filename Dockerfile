FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-dev pip
VOLUME /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt
CMD python3 index.py
