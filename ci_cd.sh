#! /bin/bash
# Demo ci/cd script that builds docker image then runs the container

# Gets web URL as parameter
url=$1

# Overwrites URL variable in .env file
echo "URL='${url}'" > .env

# Build image using docker compose
docker-compose build

# Runs image using docker compose
docker-compose up