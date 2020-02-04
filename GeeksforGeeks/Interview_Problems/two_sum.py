# YouTube Video: https://www.youtube.com/watch?v=8uYHAM-dtVA
"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
Example:
nums = [1, 3, 11, 2, 7]
target = 9
return : [3,4]
9 - 1 = 8 -> {8 : 0}
9 - 3 = 6 -> {8 : 0, 6 : 1}
9 - 11 = -2 -> {8 : 0, 6 : 1, -2 : 2}
9 - 2 = 7 -> {8 : 0, 6 : 1, -2 : 2, 7 : 3}
nums[i], i

Storing target - item in dictionary keys
Dict values we will be storing index of Previous values.
if found return the value item and the current index of the item.
"""
# Two Sum Problem

nums = [1, 3, 11, 2, 7]
target = 9

def two_sum(nums):
    if len(nums) <= 1:
        return nums
    dict = {}
    for i in range(len(nums)):
        if nums[i] not in dict:
            # Storing
            dict[target- nums[i]] = i
        else:
            return dict[nums[i]], i
print(two_sum(nums))