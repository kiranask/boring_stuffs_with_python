"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for num in nums:
            if num == 0:
                nums.remove(num)
                counter += 1
        for i in range(counter):
            nums.append(0)

        return nums

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [1, 3, 12, 0, 0]
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                # nums[zero] = num[i]

                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
        return nums






c = Solution()
d = Solution3()
print(c.moveZeroes([0,1,0,3,12]))
print(c.moveZeroes([1,0,0,1]))
print(d.moveZeroes([0,1,0,3,12]))




