FROM python:3.8-slim
RUN mkdir /opt/app
WORKDIR /opt/app
ADD requirements.txt /opt/app
RUN pip3 install -r requirements.txt
ADD . /opt/app
