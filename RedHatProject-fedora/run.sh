#!/bin/bash

APP_NAME="my-tk-app"
IMAGE_NAME="my-tk-app-image"

echo "[+] Allowing Docker access to X server"
xhost +local:docker

echo "[+] Building Docker image..."
docker build -t $IMAGE_NAME .

echo "[+] Running container..."
docker run --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    $IMAGE_NAME

echo "[+] Revoking Docker X server access"
xhost -local:docker