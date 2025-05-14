#!/bin/sh
echo "Content-type: text/plain"
echo ""
echo "Pinging..."
ping -c 2 "$(echo "$QUERY_STRING" | sed 's/^target=//')" 2>&1
