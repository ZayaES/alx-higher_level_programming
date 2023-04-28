#!/bin/bash
# connects to url and displays size of body
echo $(curl -s -o /dev/null -w "%{http_code}" "$1")
