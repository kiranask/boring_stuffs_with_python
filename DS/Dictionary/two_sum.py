"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

How to remember

“If not seen → wait for partner.
If seen → found partner.”

"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: Li st[int]
        :type target: int
        :rtype: List[int]
        """
        dic ={} #  store numbers we have seen: number → index
        for i in range(len(nums)):

            if  nums[i] not  in dic:
                # If not seen before, store the partner we will need in future
                # Example: if target=9 and nums[i]=2,
                # then we will need 7 later. So store 7 → index_of_2
                partner = target - nums[i]
                dic[partner] = i

            else:
                # If yes → we found the pair!
                # dic[nums[i]] is the index of the first number
                # i is the index of the current number
                return [dic[nums[i]], i]
            # When you hit the else branch, the current number (nums[i]) is literally the partner you stored earlier. That’s why it passes.
            """
            🔎 Example again (target = 51, nums = [13, 4, 45, 6])

            At i=2, num=45 → partner = 6 → store {6:2}

            At i=3, num=6 → this nums[i] is equal to that partner (6).

            So dic[nums[i]] = dic[6] = 2.
            """
    def two_sum(self, nums, target):
        dic = {}
        
        for item in nums:
            if item not in dic:
                dic[target-item] = item
            else:
                yield [nums.index(item), nums.index(dic[item])]

# for item in Solution().twoSum([13,4,45,6, 47,50,1], 51):
#     print(item)

for item in Solution().two_sum([13,4,45,6, 47,50,1], 51):
    print(item)


