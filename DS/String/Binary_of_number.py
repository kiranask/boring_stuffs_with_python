number = 7
bin_number = bin(number)[2:]

sum_n =0
for i in bin_number:
    sum_n += int(i)
print(sum_n)


# Aproach 2 Withoiut python

# & >>
num = 15
one_sum = 0

while num:
    one_sum += num & 1
    num >>= 1

print(one_sum)

"""
We have to get the same result 
num & 1


>>
1011
1
-----
1011
-----
  0 1 1
0011
0001
----
1111
1
-----
1111
-----


"""
