#!/bin/bash
# makes a req to 0.0.0.0:5000/catch_me that causes the server to respond with a message YOu got me
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
