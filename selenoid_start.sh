#!/bin/bash
echo "==============================> Pulling Chrome"
docker pull selenoid/vnc_chrome:83.0

echo "Starting Selenoid Service ... "
docker-compose up --force-recreate -d