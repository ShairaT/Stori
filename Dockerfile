FROM python:3.8-slim-buster

USER root

RUN apt-get update && apt-get install -y libmagic1

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP="app.py"
EXPOSE 5000

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]