#!/bin/bash

limit=0

while read LINE;
 do
   swap="0"
   book=""
   ARRAY=()

   if [ "$limit" == "$1" ]; then
     sleep 1
     limit=0
   else
     limit=$((limit+1))
   fi

   for word in $LINE
   do
     if [[ "$word" == ":" ]]; then
       swap="1"
     elif [[ "$swap" == "1" ]]; then
       ARRAY+=("$word")
     else
       book="$word"
     fi
   done;
   echo "$book is in ${ARRAY[*]}"
 done < config.arc
