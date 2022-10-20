#!/bin/bash

WORKING_DIR="$(pwd)/new-books-img"

convert_img() {
    local img_dir=$1
    local img_name
    img_name=$(find "$img_dir" | awk -F. '{ print $1}')
    convert "$img_name".jpg "$img_name".png
}

search_dir() {
    cd "$1"

    for file in *; do
        local file_dir
        file_dir=$(find "$WORKING_DIR" -name "$file")
        if [ -d "$file_dir" ]; then
            search_dir "$file_dir"
        else
            convert_img "$file_dir"
        fi
    done
}

if ! search_dir "$WORKING_DIR" 2>errors-log.txt; then
    echo "Process failed!"
else
    echo "All tasks completed!"
fi
