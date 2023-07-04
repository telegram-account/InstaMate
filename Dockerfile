FROM python:3.8-slim-buster
RUN mkdir /InstaMate && chmod 777 /InstaMate

WORKDIR /InstaMate

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt 

COPY /InstaMate .
COPY web.py .

CMD python3 __main__.py & CMD python3 web.py
