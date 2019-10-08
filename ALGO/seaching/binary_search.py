
def Binary_search(arr, start_index, last_index, element):
    while (start_index <= last_index):
        mid = (int)(start_index + last_index) / 2
        if (element > arr[mid]):
            start_index = mid + 1
        elif (element < arr[mid]):
            last_index = mid - 1
        elif (element == arr[mid]):
            return mid
    return -1

