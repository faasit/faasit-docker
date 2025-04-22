version="0.6"

ip=`hostname -i`
echo "Building faasit-spilot image with IP: $ip"
# Build the Docker image with the specified IP address
docker build --build-arg IP=$ip --no-cache -t faasit-spilot:$version .