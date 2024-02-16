#!/bin/bash

# Check if the script is executed with sudo privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run with sudo or as root" >&2
    exit 1
fi

# Check if the user provided a username as an argument
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

username="$1"

# Check if the provided username exists
if ! id "$username" &>/dev/null; then
    echo "passwd: user '$username' does not exist" >&2
    exit 1
fi

# Prompt the user to enter a new password
read -s -p "New password: " password
echo

# Prompt the user to re-enter the password for confirmation
read -s -p "Retype new password: " password_confirmation
echo

# Check if the passwords match
if [ "$password" != "$password_confirmation" ]; then
    echo "Passwords do not match" >&2
    exit 1
fi

# Change the user's password
echo "${username}:defaultPassword" | chpasswd

if [ "$?" -eq 0 ]; then
    echo "passwd: password changed successfully"
else
    echo "Sorry, passwords do not match." >&2
    echo "passwd: password unchanged" >&2
    exit 1
fi
