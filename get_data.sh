#!/bin/bash

curl -c cookies.txt -b cookies.txt https://www.space-track.org/ajaxauth/login -d "identity=$SPACETRACK_USERNAME&password=$SPACETRACK_PASSWORD"
curl --cookie cookies.txt https://www.space-track.org/basicspacedata/query/class/satcat/SATNAME/~~Starlink/orderby/LAUNCH%20asc/emptyresult/show > data.json
