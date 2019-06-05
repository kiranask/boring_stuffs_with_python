"""
Write a code to generate fibocci series in python

"""



first =0
second =1
n=10

for i in range(0,n):
    print(first)
    next = first + second
    first=second
    second=next
    i=i+1
    print(next)



