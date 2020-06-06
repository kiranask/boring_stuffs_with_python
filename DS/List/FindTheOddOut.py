"""
Given Array of Integers, every element appears
twice except for one. Find that single one


Lenear Run time

XOR : b1 | b2
       0 : 0  > 0
       0 : 1  > 1
       1 : 0  > 1
       1 :  1 > 0

"""


list = [2,3,2,3,595]
ans = []


print(2^3^2^3^595)
for numner in list:
    ans ^= numner

print(numner)