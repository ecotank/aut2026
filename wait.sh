#!/bin/bash

until curl --output /dev/null --silent --head --fail http://localhost:4444; do
    echo "Waiting for Selenium Hub..."
    sleep 1
done