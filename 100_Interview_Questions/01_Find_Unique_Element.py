"""
Write a Python program to find the unique element(s) from a list of integers, where each element may appear multiple times.


"""

def find_unique_element(lst):
    dic = {}
    for item in lst:
        if item  in dic:
            dic[item] +=1
        else:
            dic[item] =1

    repeated = []
    for key, value in dic.items():

        if value > 1:
            repeated.append(key)
    return repeated
print(find_unique_element([1,2,3,4,5,1,2]))