#!/bin/bash

regex="\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b"

if [[ $1 =~ $regex ]]; then

    if ! cat "apache.log" | grep "$1"; then
        echo "IP not found."
    fi
else
    echo "Format not valid."
fi
