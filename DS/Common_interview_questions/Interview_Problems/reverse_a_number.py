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
        # if reverse>2**31-1:
        #     return 0
        # if x<0:
        #    return reverse*-1
        # else:
        #     return reverse
        return reverse
        #if x/10 is float so we need to use x//10
    def reverse_number(self, number):

        if number < 0:
            number = number*-1
        reverse = 0
        while number > 0 :
            reminder = number%10
            reverse = reverse*10 + reminder
            number = number//10
        return reverse

print(Solution().reverse(123))
print(Solution().reverse_number(123))


