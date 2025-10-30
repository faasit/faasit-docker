FROM nvcr.io/nvidia/cuda:12.4.0-runtime-ubuntu22.04
ARG IP=192.168.28.220

# Install system dependencies
RUN apt-get update \
    && apt-get install -y software-properties-common

# Install PyTorch and torchvision with CUDA support (for GPU usage)
RUN apt install python3-pip -y

RUN pip3 install faasit-runtime[pku] --index-url http://${IP}:12121 --trusted-host ${IP} --extra-index-url https://mirrors.aliyun.com/pypi/simple/

RUN pip3 install redis psutil torch==2.5.1  torchvision==0.20.1 torchaudio==2.5.1  --index-url http://${IP}:12121 --trusted-host ${IP} --extra-index-url https://mirrors.aliyun.com/pypi/simple/

# RUN ln -s /usr/local/bin/python3 /usr/local/bin/python && ln -s /usr/local/bin/pip3 /usr/local/bin/pip

ENV FAASIT_PROVIDER=pku
