"""
Check given number is palindrome or not
"""

def isPalindrome(num):

    temp = num
    rev=0

    while temp != 0:
        rev = (rev*10)+(temp%10)
        temp = temp //10


    if num == rev:
        return True
    else :
        return False


print isPalindrome(1111)

