#!/bin/bash
# This scriptsends a DELETE request to a URL and displays the body of itd response
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f 2-
