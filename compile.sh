#!/usr/bin/env bash

# Generate the distribution archives
python3 -m pip install --upgrade build
python3 -m build

# Upload
#python3 -m pip install --upgrade twine
twine upload dist/* 
