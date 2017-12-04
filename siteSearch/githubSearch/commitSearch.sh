#!/bin/bash


for pageNum in `seq 3`
do
    curl -o temp.txt -H "Authentication: token TOKEN" \
    -H "Accept: application/vnd.github.cloak-preview" \
    https://api.github.com/search/commits?q=bit.ly&page=${pageNum:=1} ;
    sleep 2s;
    python3 commitDigest.py < temp.txt;
done
