#!/bin/bash

# Define output file
temp_file="/tmp/clipboard_image.png"
output_file="/tmp/resized_image.png"

# Get image from clipboard and save it to a temporary file
if ! command -v pngpaste &>/dev/null; then
	echo "pngpaste is not installed. Install it using: brew install pngpaste"
	exit 1
fi

pngpaste "$temp_file"

# Check if the file was created
if [[ ! -s "$temp_file" ]]; then
	echo "No image found in clipboard or clipboard does not contain an image."
	exit 1
fi

# Resize the image using ImageMagick
convert "$temp_file" -resize 1920x1080 "$output_file"

# Put the resized image back to clipboard
osascript -e 'set the clipboard to (read (POSIX file "'"$output_file"'") as «class PNGf»)'

echo "Resized image saved to $output_file and copied back to clipboard"
