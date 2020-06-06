#Filter filter out the sequnce and give the sequenve

#filter(function,iterator)
#if u want to change Every Value, you use map.
# Big data Thing
# Get the value
# filter value
# map the value - Perform some operation +-some thing like that.
# reduce the value and give: use these value and get some thing
# reduce at one time it uses two values.
from functools import reduce

nums = [1,2,3,4,5,6,7,8]
evens = list(filter(lambda x:x%2==0,nums))
double = list(map(lambda x :x*2,evens))
print(double)
sum = reduce(lambda a,b:a+b,double)
print(sum)