#!/bin/sh

sudo apt-get update
sudo apt-get remove docker docker-engine docker.io -y
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo apt install docker-compose -y
docker-compose build 
docker-compose up
docker-compose up -d