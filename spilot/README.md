## faasit-spilot

### 0.4

```bash
git clone --branch criu-test https://github.com/ProjectMitosisOS/mitosis-core.git
wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz -O Python-3.10.12.tgz
```

```bash
docker build -t criu-base -f Dockerfile.criu .
docker build -t spilot-python-env -f Dockerfile.python .
docker build -t faasit-spilot-base -f Dockerfile.faasit .
docker build -t faasit-spilot:0.4 .
```

### 0.6

```bash
git clone --branch criu_develop --depth 1 https://github.com/greenEggLy/mitosis-core.git
```