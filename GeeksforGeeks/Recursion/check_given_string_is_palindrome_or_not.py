'''Given a string, the task is to write a recursive function to check if the given string is palindrome or not.
'''

# given_string
# upper - upper bound
# lower - lower bound


def palindrome(string_check, lower, upper):

    if string_check[lower] == string_check[upper]:
        return True


    if string_check[lower] != string_check[upper]:
        return False


    return palindrome(string_check,lower+1,upper-1)

given_string ="malayalam"

lower_char= 0
upper_char= len(given_string)-1


print (palindrome(given_string,lower_char,upper_char))




