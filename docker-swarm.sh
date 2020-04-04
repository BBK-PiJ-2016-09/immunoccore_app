# Build the image from current repo status
docker build -t immunocore_image .

# Start docker swarm ...
docker swarm init

# Make a network so nodes can talk
docker network create immunocore_network --driver overlay --subnet=192.168.100.0/24

# Create the postgres
docker service create --name postgres --network immunocore_network --env POSTGRES_PASSWORD=docker \
    --env POSTGRES_USER=docker --env POSTGRES_DB=docker postgres


# Start the service and publicc ports
docker service create --name immunocore --replicas 3 --network immunocore_network \
    --env SQLALCHEMY_DATABASE_URI='postgresql://docker:docker@postgres/docker?keepalives=1&keepalives_idle=10' \
    --publish published=80,target=8000 --publish published=8000,target=5000 immunocore_image
