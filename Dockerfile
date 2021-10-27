FROM ubuntu:latest

MAINTAINER Sreeraj


RUN apt-get -y update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y


RUN mkdir /qure_assignment

WORKDIR /qure_assignment


ADD . /qure_assignment/

RUN pip install --no-cache-dir -r requirements.txt

