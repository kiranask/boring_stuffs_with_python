"""

Check given number is palindrome or not


Kill_telGagaga

"""

def isPalindrome(x):

    number = str(x)
    """
    
    Comparing the first character of the string with last charcter of the string
    
    """
    left, right =0, len(number)-1

    while right>left :
        if number[left]!=number[right]:return False
        left +=1
        right-=1
    return True

print(isPalindrome(1233211))