FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD src/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD ./src/ /code/

EXPOSE 8030