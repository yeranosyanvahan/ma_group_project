#!/bin/bash

pip3 install pyment
find . -type f -name "*.py" | while read file; do
    echo "Processing $file..."
    pyment -w -o numpydoc "$file"
done

echo "All .py files processed."
