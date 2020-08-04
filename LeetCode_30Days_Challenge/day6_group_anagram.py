"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


def anagram_checker(items):
    dic = {}
    for item in items:
        sorted_word = "".join(sorted(item))
        if sorted_word not in dic:
            dic[sorted_word] = [item]
        else:
            dic[sorted_word].append(item)
    result = []
    for item in dic.values():
        result.append(item)
    return sorted(result)


print(anagram_checker(["eat", "tea", "tan", "ate", "nat", "bat"]))

