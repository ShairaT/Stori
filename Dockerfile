FROM python:3.8-slim-buster

USER root

RUN apt-get update && apt-get install -y libmagic1

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FIREBASE_API_KEY="AIzaSyDlsV5xEx31i1hXqfW-XfS8e3vdMBnT62k"
ENV FIREBASE_AUTH_DOMAIN="stori-7daed.FIREBASEapp.com"
ENV FIREBASE_PROJECT_ID="stori-7daed"
ENV FIREBASE_DATABASE_URL="https://stori-7daed-default-rtdb.firebaseio.com"
ENV FIREBASE_STORAGE_BUCKET="stori-7daed.appspot.com"
ENV FIREBASE_MESSAGING_SENDER_ID="57845009728"
ENV FIREBASE_APP_ID="1=57845009728=web=5198d7cb66eb7c6d79bea5"
ENV FIREBASE_MEASUREMENT_ID="G-MB96FPLM62"
ENV SENDGRID_API_KEY="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"
ENV ENCRYPTION_KEY="suRZHEWszqS6MkT__MjfdvZ7QGYTkAw5U7bV9g0FSFk="
ENV FLASK_APP="app.py"
EXPOSE 5000

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]