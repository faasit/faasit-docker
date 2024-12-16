FROM ubuntu:18.04 AS criu-base

# RUN sed -i s/archive.ubuntu.com/mirror.sjtu.edu.cn/g /etc/apt/sources.list && \
#     sed -i s/security.ubuntu.com/mirror.sjtu.edu.cn/g /etc/apt/sources.list
# RUN rm -rf /var/lib/apt/lists/*

COPY aliyun.list /etc/apt/sources.list

RUN apt update && apt upgrade -y

RUN mkdir -p /mitosis

WORKDIR /mitosis

RUN apt install -y git cmake build-essential

# RUN GIT_SSL_NO_VERIFY=1 git clone --branch criu-test https://github.com/ProjectMitosisOS/mitosis-core.git
COPY mitosis-core /mitosis/mitosis-core

RUN cd mitosis-core/mitosis-user-libs/mitosis-lean-container/lib \
    && mkdir build && cd build \
    && cmake .. \
    && make
COPY run.sh /mitosis/
RUN chmod +x /mitosis/run.sh

# install criu 
RUN apt install -y criu

# install python
# RUN apt update && apt install -y python3 wget && wget https://bootstrap.pypa.io/pip/3.5/get-pip.py && python3 get-pip.py && rm -rf /var/lib/apt/lists/*

FROM criu-base AS python-env

# RUN apt install python3 python3-pip -y

# 设置时区为Asia/Shanghai（或你需要的其他时区）
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y tzdata \
    && ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt install -y \
build-essential \
zlib1g-dev \
libncurses5-dev \
libncursesw5-dev \
libreadline-dev \
libsqlite3-dev \
libgdbm-dev \
libdb-dev \
libbz2-dev \
liblzma-dev \
libssl-dev \
libffi-dev \
uuid-dev \
tk-dev \
libbluetooth-dev \
libbluetooth3 \
libdb5.3-dev wget

COPY Python-3.10.12.tgz .

RUN tar -zxvf Python-3.10.12.tgz && rm Python-3.10.12.tgz && cd Python-3.10.12 && ./configure --enable-optimizations && make -j$(nproc) && make install

COPY requirements.txt .
RUN pip3 install -r requirements.txt -i https://mirror.sjtu.edu.cn/pypi/web/simple

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

FROM python-env AS spilot-base

RUN pip3 install faasit-runtime --index-url http://192.168.28.220:12121 --trusted-host 192.168.28.220 

RUN ln -s /usr/local/bin/python3 /usr/local/bin/python && ln -s /usr/local/bin/pip3 /usr/local/bin/pip

ENV FAASIT_PROVIDER=pku