"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

from sys import maxint
def maxSubArraySum(a,size):

    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

"""
from sys import maxsize

'''
logic:
#1: Add all positive contigeous elements
#2: if max_sofar < sum, update the max_sofar
# if sum < 0, update it to 0, sum = 0 , because sum cannot be 0 all the time.

'''
def max_subarray(nums):
    max_sofar = -9999
    sum = 0
    for i in range(0, len(nums)):
        sum = nums[i] + sum
        # Update max so far
        if max_sofar < sum :
            max_sofar = sum
        if sum < 0 :
            sum = 0
    return max_sofar


from sys import maxsize


def maxSubArraySum(a):
    max_so_far = -9999
    max_ending_here = 0

    for i in range(0, len(a)):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
