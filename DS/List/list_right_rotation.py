# def right_rotation(arr,d):
#     for i in range(d):
#         one_right_rotate(arr)
#     return arr
#
# def one_right_rotate(arr):
#     for i in range( len(arr)-1):
#        print(arr[i])
#
# # print(right_rotation([1,2,3,4,5,6],2))
# print(one_right_rotate([1,2,3,4]))

list = [1,2,3,4,5]
for i in range(1,len(list)):
    list[i] = list[i+1]
print()
