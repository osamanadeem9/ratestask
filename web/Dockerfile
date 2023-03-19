FROM python:3.8.3-slim-buster
# RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

COPY . /web
WORKDIR /web

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python3", "app.py"]