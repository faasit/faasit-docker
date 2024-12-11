### Run criu with Ubuntu environment in python3.10 (Debian) container
#### Build Ubuntu image as rootfs
```bash
# Assume in ~/mitosis
docker build -t criu -f Dockerfile.ubuntu .

# Run this image
docker run -it --rm --privileged --name criu criu /bin/bash
# In the container, use criu to dump
# Should be successful
bash checkpoint.sh

# Outside the container (in ~/mitosis), but don't stop it
docker export criu -o criu.tar
# Now container can be stopped
mkdir .base
tar -C .base/ -xf criu.tar

# clean
rm criu.tar
```


#### Build python3.10 image and test

```bash
# Assume in ~/mitosis
# may need change python3.10 in dockerfile to other image (e.g. chameleom-stage0:tmp)
sudo docker build -t criu_test -f Dockerfile.criu .

# enter container
docker run -it --rm --privileged criu_test /bin/bash
# run test
bash run.sh
```

#### Build faasit-spilot

```bash
docker build -t faasit-spilot:0.3 --no-cache .
```