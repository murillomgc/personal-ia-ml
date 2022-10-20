#!/bin/bash

if [ -z $1 ]; then
    while [ -z $request ]; do
        read -p "Type one of the valid parameter (GET|PUT|POST|DELETE): " request
        upper_input=$(echo $request | awk '{print toupper($1)}')
    done
else

    upper_input=$(echo $1 | awk '{print toupper($1)}')
fi

case $upper_input in
GET)
    cat cat apache.log | grep GET
    ;;
POST)
    cat apache.log | grep POST
    ;;
PUT)
    cat apache.log | grep PUT
    ;;
DELETE)
    cat apache.log | grep DELETE
    ;;
*)
    echo "Invalid parameter."
    ;;
esac
