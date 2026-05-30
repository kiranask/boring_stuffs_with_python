"""
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

"""
from boring_stuffs_with_python.DS.Stack.reverse_string_using_stack import reverse


class Solution:
    def numberOfSpecialChars(self, words: str) -> int:

        char_set = set(words)
        counter = 0
        for word in char_set:
            if word.islower() and word.upper() in  char_set:
                counter +=1
        return counter


solve = Solution()

print(solve.numberOfSpecialChars("aaAbcBC"))




