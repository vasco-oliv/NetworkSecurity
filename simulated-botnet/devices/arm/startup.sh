#!/bin/sh

echo "Starting vulnerable HTTP server..."
httpd -p 80 -h /www -c /www/httpd.conf

while true; do sleep 60; done
