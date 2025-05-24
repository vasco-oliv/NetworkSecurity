#!/bin/bash

# List of device IPs
MIPS_DEVICES=(
  172.20.0.2  # mips1
  172.20.0.3  # mips2
  172.20.0.4  # mips3
)

ARM_DEVICES=(
  172.20.0.5  # arm1
  172.20.0.6  # arm2
  172.20.0.7  # arm3
)

# Loop through each IP and run the script
for IP in "${MIPS_DEVICES[@]}"; do
  echo "Running script.py for $IP"
  python3 script.py "$IP" 2
done

for IP in "${ARM_DEVICES[@]}"; do
  echo "Running script.py for $IP"
  python3 script.py "$IP" 1
done
