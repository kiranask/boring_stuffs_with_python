class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {}
        paris = []

        for i in range(len(nums)):

            y = target - nums[i]

            if y not in dictionary:
                dictionary[i] = y
            else:
                pairs.extend(i, nums.index(dictionary[i]))

        return paris
