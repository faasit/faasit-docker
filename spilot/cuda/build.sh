version="0.1"

ip=`hostname -i`
echo "Building faasit-spilot-cuda image with IP: $ip"
# Build the Docker image with the specified IP address
docker build --network host --build-arg IP=$ip --no-cache -t faasit-spilot-cuda:$version .
