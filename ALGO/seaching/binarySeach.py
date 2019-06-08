class BinarySearch:

    def search(self, arr, val):
        return self.binarySearch(arr, 0, len(arr)-1, val)

    def binarySearch(self, arr, start, end, val):
        mid_index = (start+end)//2
        if start <= end:
            if arr[mid_index] == val:
                return mid_index
            if val > arr[mid_index]:
                return self.binarySearch(arr, mid_index+1, end, val)
            elif val < arr[mid_index]:
                return self.binarySearch(arr, start, mid_index-1, val)
        return -1

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60, 70]
    obj = BinarySearch()
    print(obj.search(arr, 70))
