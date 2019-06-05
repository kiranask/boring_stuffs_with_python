list1 =[1,2,3,4,6,3,5,4,6]

arr = list(set(list1))
largest = max(arr)
arr.remove(largest)
print(max(arr))
