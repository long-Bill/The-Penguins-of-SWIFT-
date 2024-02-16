#!/bin/bash

# Check if counter file exists, if not create it
COUNTER_FILE="/root/counter.txt"
if [ ! -f "$COUNTER_FILE" ]; then
    echo "0" > "$COUNTER_FILE"
fi

# Read the current counter value
COUNTER=$(<"$COUNTER_FILE")

# Increment the counter
((COUNTER++))

# Add user with incremented username
USERNAME="user$COUNTER"
useradd -m -d /home/"$USERNAME" -s /bin/bash -g root "$USERNAME"
usermod -a -G sudo "$USERNAME"

echo "$USERNAME" added

# Update counter file
echo "$COUNTER" > "$COUNTER_FILE"
