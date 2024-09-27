#!/bin/bash
count=0
num=10
while [[ count -lt num ]]
do
  echo $count
  # shellcheck disable=SC1068
  (( count += 1 ))
done