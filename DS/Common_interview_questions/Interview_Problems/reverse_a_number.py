"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        n =x
        if n<0:
            n=n*-1

        reverse=0
        while n>0:
            reminder = n%10
            reverse= reverse*10+reminder
            n=n//10
        #Supporting only 32 bit integer
        if reverse>2**31-1:
            return 0
        if x<0:
           return reverse*-1
        else:
            return reverse

        #if x/10 is float so we need to use x//10


print(Solution().reverse(1212))


