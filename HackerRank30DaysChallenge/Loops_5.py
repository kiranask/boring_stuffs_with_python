#!/bin/python3

import math
import os
import random
import re
import sys

def maggi(n):
    if 2<= n <= 20:
        for i in range(1,11):
            print(str(n)+" x "+str(i)+" = "+str(n*i))


if __name__ == '__main__':
    n = int(input())
    maggi(n)

