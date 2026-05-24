"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from DS import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for str in strs:
            if len(str) == 0:
                return ""
            common_prefix = str[0]
            for i in range(1, len(str)):
                if str[i] != common_prefix:
                    return common_prefix
