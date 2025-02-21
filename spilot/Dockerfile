ARG HTTP_PROXY
ARG HTTPS_PROXY

FROM faasit-spilot-base AS node-env

ENV http_proxy=$HTTP_PROXY
ENV https_proxy=$HTTPS_PROXY

# ENV NODE_VERSION=v16.20.2

# RUN wget http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.gz -O /tmp/node-${NODE_VERSION}-linux-x64.tar.gz \
#     && cd /tmp && tar -zxvf /tmp/node-${NODE_VERSION}-linux-x64.tar.gz \
#     && mv /tmp/node-${NODE_VERSION}-linux-x64 /opt/node

# ENV PATH=$PATH:/opt/node/bin

RUN apt update && apt install -y curl

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl https://get.volta.sh | bash

ENV PATH=$PATH:/root/.volta/bin

ENV VOLTA_FETCH_NODE="https://mirrors.cloud.tencent.com/node"

# ENV https_proxy=http://114.212.80.7:21087

RUN volta install node@16.20.2 && volta install pnpm@7

# ENV https_proxy=""

RUN mkdir -p /node_modules

RUN pnpm config set registry https://registry.npmmirror.com

COPY ./node/faasit-runtime /node_modules/faasit-runtime

RUN npm install -g /node_modules/faasit-runtime --registry=https://registry.npmmirror.com/


FROM node-env AS faasit-spilot

RUN apt remove curl wget -y && apt autoremove -y