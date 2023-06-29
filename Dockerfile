FROM python:3.8-slim-buster
RUN mkdir /InstaMate && chmod 777 /InstaMate

WORKDIR /InstaMate

COPY dockerImage.txt dockerImage.txt
RUN pip install --upgrade pip && pip install -r dockerImage.txt 

COPY . .

CMD python3 InstaMate
