import sys


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, item):
        self.stack.append(item)

    def enqueueCharacter(self, item):
        self.queue.insert(0, item)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop()

    # Write your code here


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")