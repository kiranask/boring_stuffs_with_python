from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        dict ={}
        sub_arr,count = 0,0
        for i in range(len(nums)):
            if nums[i] ==1:
                count += 1
            else:
                count -= 1
            if count == 0:
                sub_arr = i+1
            if count not in dict:
                dict[count] = i
            else:
                sub_arr = max( sub_arr , i-dict[count])
                # sub_arr > Previous value
                # i - last occurance of the dict[count]
        return sub_arr