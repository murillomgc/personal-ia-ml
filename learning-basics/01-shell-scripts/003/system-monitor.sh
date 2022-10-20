#!/bin/bash

if [ ! -d log ]; then
    mkdir log
fi

memory_search() {

    process_list=$(ps -e -o pid --sort -size | head -n 11 | grep "[0-9]")

    for pid in $process_list; do
        process_name="$(ps -p "$pid" -o comm=)"
        process_size=$(ps -p "$pid" -o size | grep "[0-9]")

        echo -n "$(date "+%F,%H:%M:%S",)" >>"log/$process_name.log"
        echo "$(bc <<<"scale=2;$process_size/1024") MB" >>"log/$process_name.log"
    done
}

if ! memory_search 2>errors-log.txt; then
    echo "Process failed!"
else
    echo "All tasks completed!"
fi
