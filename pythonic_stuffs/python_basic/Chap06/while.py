#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''

while pw != secret:
    pw = str(input("What's the secret word? "))
    if len(pw)==0:
        print("Please enter password")
    elif pw.isnumeric():
        print("Enter String value")
    else:
        print("Wrong password!")
