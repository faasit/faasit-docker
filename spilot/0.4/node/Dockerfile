FROM faasit-spilot:0.3

ENV NODE_VERSION=v22.12.0

RUN wget http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.gz -O /tmp/node-${NODE_VERSION}-linux-x64.tar.gz \
    && cd /tmp && tar -zxvf /tmp/node-${NODE_VERSION}-linux-x64.tar.gz \
    && mv /tmp/node-${NODE_VERSION}-linux-x64 /opt/node

ENV PATH=$PATH:/opt/node/bin

RUN mkdir -p /node_modules

COPY faasit-runtime /node_modules/faasit-runtime

RUN npm install -g /node_modules/faasit-runtime

RUN npm install -g pnpm --registry=https://registry.npmmirror.com/