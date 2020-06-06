#!/bin/python3

import math
import os
import random
import re
import sys


def convert_binary(number):
    binary = ""
    if number == 0:
        binary = binary + "0"
    if number >= 1:
        while (number >= 1):
            if number % 2 == 0:
                binary = binary + "0"
                number = number // 2
            else:
                binary = binary + "1"
                number = (number - 1) // 2

    binary_number = "".join(reversed(binary))
    # return (binary_number)
    count = 0
    for i in range(len(binary_number) -1):
        if binary_number[i] == 1:
            count = 1

        





print(convert_binary(13))
