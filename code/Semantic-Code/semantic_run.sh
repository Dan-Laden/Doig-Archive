#!/bin/bash

limit=0
flag=0

while read LINE;
 do
   swap="0"
   book=""
   ARRAY=()

   if [[ "$limit" == "$1" ]] && [[ "$flag" == 0 ]]; then #command "${my_array[@]/#/-}"
     python3 Semantic_Enhancement.py --new ${PARAMETERS[@]}
     sleep 600
     limit=0
     PARAMETERS=()
     flag=1
   elif [[ "$limit" == "$1" ]]; then
     python3 Semantic_Enhancement.py --old ${PARAMETERS[@]}
     sleep 600
     PARAMETERS=()
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
       ARRAY+=("$word")
     fi
   done;
   ARRAY+=(" ")
   PARAMETERS+=${ARRAY[@]}
 done < config.arc
 python3 Semantic_Enhancement.py --old ${PARAMETERS[@]}
 python3 Relation_Builder.py


##################################################################
#Resources used while learning how to write this is bash
#https://stackoverflow.com/questions/14511295/bash-integer-comparison
#https://unix.stackexchange.com/questions/232384/argument-string-to-integer-in-bash
#https://askubuntu.com/questions/385528/how-to-increment-a-variable-in-bash
#https://stackoverflow.com/questions/41150814/how-to-echo-all-values-from-array-in-bash
#http://www.tldp.org/LDP/abs/html/abs-guide.html#VARIABLES
#https://stackoverflow.com/questions/16203088/bash-if-statement-with-multiple-conditions-throws-an-error
#https://unix.stackexchange.com/questions/29509/transform-an-array-into-arguments-of-a-command
##################################################################
