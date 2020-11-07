FROM python:3.8-slim
RUN mkdir /api
WORKDIR /api
ADD requirements.txt /api
RUN pip3 install -r requirements.txt
ADD . /api
EXPOSE 3000
CMD gunicorn --bind 0.0.0.0:$PORT app:app