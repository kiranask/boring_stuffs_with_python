# # First Method to Create 1-D Array:
# n = 5
# arr = [0] * n
# print(arr)
#
# # Second Method to Create 2-D Array:
# n = 5
# arr = [i for i in range(10)]
# print(arr)
#
# # Using
#
# # Using First Method To Create 2-d Array:
#
r,c  = 5,4
# two_d_arr = [[0] * r] * c
# print(two_d_arr)





count = 0
two_d_f0 = [ [i for i in range(c)] for j in range(r) ]

print(two_d_f0)

for i in range(r):
    a = []
    for j in range(c):
        a.append()