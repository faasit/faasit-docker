FROM python:3.10

WORKDIR /app

COPY ./src /app
COPY ./requirements.txt /app/requirements.txt
COPY ./faasit-runtime /faasit-runtime

RUN pip install --upgrade pip

# RUN pip install -r requirements.txt
RUN pip install "flask[async]"

RUN pip install -e /faasit-runtime

RUN mkdir -p /code && cd /code

WORKDIR /code

ENV FAASIT_PROVIDER local

CMD [ "bash" ]