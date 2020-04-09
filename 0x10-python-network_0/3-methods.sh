#!/bin/bash
# cURL only methods
curl -sI 0.0.0.0:5000/route_4 | grep -i Allow: | awk -F": " '{print $2}'
