"""
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .
"""
#
# Sample Input 0
#
# aba
# 10
# Sample Output 0
#
# 7
# Explanation 0
# The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.
#
# Sample Input 1
#
# a
# 1000000000000
# Sample Output 1
#
# 1000000000000

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    return s.count('a') * (n//len(s))+ s[:(n%len(s))].count('a')
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(str(result) +'\n')

    # fptr.write(str(result) + '\n')

    # fptr.close()