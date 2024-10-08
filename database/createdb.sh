#!/bin/bash

# Build the Docker image
docker build -t postgres-db .

# Exit if the build failed
if [ $? -ne 0 ]; then
  exit 1
fi

# Run the Docker container with environment variables from .env
docker run --rm --env-file .env \
  --name postgres-container \
  -p 5432:5432 \
  -d postgres-db