FROM python:3.6.1
ENV PYTHONUNBUFFERED 1

WORKDIR /srv/djb_django

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
