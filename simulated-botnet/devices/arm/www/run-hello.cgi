#!/bin/sh
echo "Content-type: text/plain"
echo ""

# Execute the 'hello' file and print its output
if [ -x "./hello" ]; then
    echo "Running 'hello'..."
    ./hello 2>&1
else
    echo "'hello' not found or not executable."
fi

