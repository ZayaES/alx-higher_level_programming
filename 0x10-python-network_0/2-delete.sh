#!/bin/bash
# connects to url and displays size of body
curl -X DELETE -i "$1" | awk '{if(NR>1)print}'
