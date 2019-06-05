arr=[10,-2,1,-3,0,9]

def find_largest(arr):
    largest = arr[0]
    if len(arr)==0:
        return None

    for element in arr:
        if element > largest:
            largest = element
    return largest
try:
    arr.remove(find_largest(arr))
except:
    print "Small array"
print "The second largest element is ",find_largest(arr)