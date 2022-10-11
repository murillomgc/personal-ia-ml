#!/bin/bash

converter() {
    local INPUT=books-jpg
    local OUTPUT=books-png
    local DIR_INPUT
    local DIR_OUTPUT
    local IMG_NAME

    DIR_INPUT=$(pwd)/"$INPUT"
    DIR_OUTPUT=$(pwd)/"$OUTPUT"

    if [ ! -d "$DIR_OUTPUT" ]; then
        mkdir "$OUTPUT"
    fi

    for img in "$DIR_INPUT"/*.jpg; do
        IMG_NAME=$(find "$img" | awk -F. '{ print $1}')
        convert "$IMG_NAME".jpg "$IMG_NAME".png
    done

    for imgpng in "$DIR_INPUT"/*.png; do
        mv "$imgpng" "$DIR_OUTPUT"
    done
}

if ! converter 2>errors_log.txt; then
    echo "Process failed!"
else
    echo "All tasks completed!"
fi
