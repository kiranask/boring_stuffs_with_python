"""
Input:  [8, 1, 2, 2, 3]

Output: [4, 0, 1, 1, 3]
"""

nums= [8, 1, 2, 2, 3]
sorted_nums = sorted(nums)
# [1,2,2,3,8]


result = []

for num in nums:
    result.append(sorted_nums.index(num))
print(result)

dict_index = {}

return_list = []
for i, value in enumerate(sorted_nums):

    dict_index[value] = i

print(dict_index)

for num in nums:
    return_list.append(dict_index[num])

print(return_list)