def is_palindrome(given_string):
    if len(given_string) <=1:
        return True


    else :
        return given_string[0]==given_string[-1] and is_palindrome(given_string[1:-1])

print(is_palindrome("malayalam"))