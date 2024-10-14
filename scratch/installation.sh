#!/bin/bash

docker pull node:20-alpine

# Checking the version it should be v20.18.0
docker run node:20-alpine node -v
# Checking the npm version it should be 10.8.2
docker run node:20-alpine npm -v


