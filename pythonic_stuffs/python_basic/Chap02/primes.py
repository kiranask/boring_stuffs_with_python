#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):

    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

print (isprime(21))

