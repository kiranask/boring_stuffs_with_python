"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.

For example, alison heck should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.

"""


# Complete the solve function below.


import os
import math
import os
import random
import re
import sys


def solve(s):

# Inorder to loop through the string split use for loop

# Replace word using s.replace(x, x.capitalize())
    for x in s[:].split():
        s = s.replace(x, x.capitalize())

#capitalize() --> Capitalize  the first letter
    print(s)

if __name__ == '__main__':
    s= "geeks for geeks"
    solve(s)
