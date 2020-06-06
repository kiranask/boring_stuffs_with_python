
from itertools import zip_longest

# Enter your code here. Read input from STDIN. Print output to STDOUT
red_flowers = input()
white_flowers = input()



def garland_maker(s,t):
    if not (s and t):
        return s + t
    else:
        return s[0] + t[0] + garland_maker(s[1:],t[1:])
    # return ''.join(chain(*zip_longest(s, t, fillvalue='')))


garland_maker(red_flowers, white_flowers)
#
#
# print(''.join(val for pair in zip(list1, list2) for val in pair) + list1[-1])


