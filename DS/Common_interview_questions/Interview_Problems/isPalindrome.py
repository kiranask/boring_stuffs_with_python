"""
Check given number is palindrome or not
123

321

123%10

reverse = 3

3 * 10 = 30

12



rev = 0 + 3
temp = 12


rev = 30 + 2
temp = 2


rev = 32*10 + 1

tem =
"""



def isPalindrome(num):
    temp = num
    rev= 0
    while temp != 0:
        print(rev)
        rev = (rev*10)+(temp%10)
        temp = temp //10
    return rev
print( isPalindrome(123))

