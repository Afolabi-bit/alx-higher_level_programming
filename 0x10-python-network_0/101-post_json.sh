#!/bin/bash
# This script sends a JSON post req to a URL, displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
