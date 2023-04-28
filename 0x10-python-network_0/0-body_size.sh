#!/bin/bash
# connects to url and displays size of body
curl -s -o /dev/null -w "%{size_download}" "$1"
echo
