<<<<<<< HEAD
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
=======
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
>>>>>>> db4c213626872d030fcee66400649bf5f9821f2f
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app