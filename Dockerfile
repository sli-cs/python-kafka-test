FROM python:3.6.1
ADD ./src/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD ./src /code
WORKDIR /code
