version="1.0"

ip=`hostname -i`
echo "Building faasit-runtime image with IP: $ip"
# Build the Docker image with the specified IP address
docker build --build-arg IP=$ip --no-cache -t faasit-runtime:$version .