#!/bin/bash

# Create the service-result directory on the local machine if it doesn't exist
mkdir -p service-result/

# Get the running container ID
CONTAINER_ID=$(docker ps -q)

# Check if a container is running
if [ -z "$CONTAINER_ID" ]; then
    echo "Error: No running container found."
    exit 1
fi

echo "Copying output files from the container to the local machine..."

# Copy output files from the container to bd-a1/service-result/ on the local machine
docker cp "$CONTAINER_ID":/home/doc-bd-a1/res_dpre.csv service-result/
docker cp "$CONTAINER_ID":/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp "$CONTAINER_ID":/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp "$CONTAINER_ID":/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp "$CONTAINER_ID":/home/doc-bd-a1/vis.png service-result/
docker cp "$CONTAINER_ID":/home/doc-bd-a1/k.txt service-result/

echo "Files successfully copied to bd-a1/service-result/"

# Stop the running container
docker stop "$CONTAINER_ID"
echo "Container stopped."