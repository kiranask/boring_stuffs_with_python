from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                # Store the index of the the current num with its index.
                return [i, num_map[complement]]
            else:
                num_map[nums[i]] = i
        return []


sol = Solution()
print(sol.twoSum(nums=[2,7,11,15], target=9))