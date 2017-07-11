FROM python:2.7
MAINTAINER JMOZ james@jmoz.co.uk

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE moj.settings

RUN mkdir /code
WORKDIR /code
ADD moj /code/

RUN pip install -r requirements.txt
RUN python manage.py test