FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN apt-get update && apt-get install -y netcat libpq-dev python3.8-dev supervisor

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
RUN ["chmod", "+x", "entrypoint.sh"]
CMD ["./entrypoint.sh"]
