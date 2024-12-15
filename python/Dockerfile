FROM python:3.10

WORKDIR /app

COPY ./src /app

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip install "flask[async]"

RUN pip install faasit-runtime --index-url http://192.168.28.220:12121 --trusted-host 192.168.28.220 

RUN mkdir -p /code && cd /code

WORKDIR /code

ENV FAASIT_PROVIDER=local

CMD [ "bash" ]