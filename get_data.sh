#!/bin/bash

# Obtain cookies for authentication
curl -c cookies.txt -b cookies.txt https://www.space-track.org/ajaxauth/login -d "identity=$SPACETRACK_USERNAME&password=$SPACETRACK_PASSWORD"

# Get data
curl --cookie cookies.txt https://www.space-track.org/basicspacedata/query/class/satcat/SATNAME/~~Starlink/orderby/LAUNCH%20asc/emptyresult/show > starlink_satcat.json
sleep 2 # Ethical downloading
curl --cookie cookies.txt https://www.space-track.org/basicspacedata/query/class/satcat/SATNAME/~~OneWeb/orderby/LAUNCH%20asc/emptyresult/show > oneweb_satcat.json
sleep 2
curl --cookie cookies.txt https://www.space-track.org/basicspacedata/query/class/satcat/SATNAME/~~O3B/orderby/LAUNCH%20asc/emptyresult/show > o3b_satcat.json
sleep 2
curl --cookie cookies.txt https://www.space-track.org/basicspacedata/query/class/satcat/SATNAME/~~Kuiper/orderby/LAUNCH%20asc/emptyresult/show > kuiper_satcat.json

