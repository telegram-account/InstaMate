FROM python:3.8-slim-buster
RUN mkdir /InstaMate && chmod 777 /InstaMate

WORKDIR /InstaMate

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt 

COPY /InstaMate .
COPY web.py .

EXPOSE 8000

CMD gunicorn web:app & python3 main.py
