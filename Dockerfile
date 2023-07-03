FROM python:3.8-slim-buster
RUN mkdir /InstaMate && chmod 777 /InstaMate

WORKDIR /InstaMate/

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt 


RUN find . -type d
COPY . .

CMD python3 /InstaMate/__main__.py
