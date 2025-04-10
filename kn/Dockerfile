FROM python:3.10-slim

ARG IP=192.168.28.220
RUN pip install flask

RUN pip install faasit_runtime[kn] --no-cache --index-url http://${IP}:12121 --trusted-host ${IP}

RUN mkdir -p /code && cd /code

WORKDIR /code

ENV FAASIT_PROVIDER=knative 

CMD ["bash"]