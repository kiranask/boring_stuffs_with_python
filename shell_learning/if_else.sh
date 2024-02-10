#!/bin/bash

<<comment
equal
-eq : For Numerical value
== : for String
-ge
-le
!=
-ne
-gt
-le

comment
read -p "Enter your Marks" marks

# shellcheck disable=SC1046
if [[ $marks -gt 40 && $marks -lt 50 ]]
then
  echo "You are pass"
elif [ "$marks" == 40 ];
then
  echo "Just pass"

elif [[ $marks -le 80 && $marks -ge 60 ]]
then
  echo "First Class"

else
  echo "You are fail!!"
fi


