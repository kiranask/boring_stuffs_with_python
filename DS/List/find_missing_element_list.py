"""
Two Arrays
Second array is formed by shuffling the first list

"""

def find_missing(list1, list2):
    for item in list1:
        if item not in list2:
            yield item

for item in find_missing([1,2,3,4,5], [1,2,4]):
    print(item)
