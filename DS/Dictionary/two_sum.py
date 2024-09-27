"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].


"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: Li st[int]
        :type target: int
        :rtype: List[int]
        """
        dic ={}
        for i in range(len(nums)):
            if  nums[i] not  in dic:
                dic[target - nums[i]] = i
            else:
                yield dic[nums[i]],i

    def two_sum(self, nums, target):
        dic = {}
        
        for item in nums:
            if item not in dic:
                dic[target-item] = item
            else:
                yield [item, dic[item]]

# for item in Solution().twoSum([13,4,45,6, 47,50,1], 51):
#     print(item)

for item in Solution().two_sum([13,4,45,6, 47,50,1], 51):
    print(item)


