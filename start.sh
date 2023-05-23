#!/bin/bash
app="capstone"
docker build -t ${app} .
docker run \
    -it \
    --rm \
    -p 3000:80 \
    --name ${app} \
    ${app}
