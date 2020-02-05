# Python3 code to move all zeroes
# at the end of array
def pushZerosToEnd(arr):
    n = len(arr)
    count = 0 # Count of non-zero elements
    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1
