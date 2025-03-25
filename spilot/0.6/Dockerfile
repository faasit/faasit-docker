FROM python:3.10-slim

RUN pip3 install faasit-runtime[pku] --index-url http://192.168.28.220:12121 --trusted-host 192.168.28.220 

# RUN ln -s /usr/local/bin/python3 /usr/local/bin/python && ln -s /usr/local/bin/pip3 /usr/local/bin/pip

ENV FAASIT_PROVIDER=pku
