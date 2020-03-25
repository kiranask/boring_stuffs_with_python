#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    current = 0
    end = len(c) -1

    while current < end:
        # When to do the double jump
        if (current +2) <= end  and (c[current+2]==0):
            current += 2
            jumps +=1
        # When to Do the Single Jump
        elif c[current+1] == 0:
            jumps += 1
            current +=1

    return jumps

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
