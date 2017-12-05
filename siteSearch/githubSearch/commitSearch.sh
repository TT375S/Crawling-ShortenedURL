#!/bin/bash


for pageNum in `seq 3`
do
    #curl -o temp.txt -H "Authentication: token TOKEN" \
    #-H "Accept: application/vnd.github.cloak-preview" \
    #https://api.github.com/search/commits?q=bit.ly&page=$( echo "${pageNum}");
    
    curl -H "Authentication: token TOKEN"     -H "Accept: application/vnd.github.cloak-preview"   "https://api.github.com/search/commits?q=bit.ly&per_page=100&page=$(echo "${pageNum}" )"  |    python3 commitDigest.py; 

    echo pageNum = $( echo "${pageNum}")
done
