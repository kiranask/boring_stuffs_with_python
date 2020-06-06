#malayalam

import string
def is_palindrome(word):
    word = word.lower()
    word = word.translate("None",string.punctuation)
    word = word.replace(" ","")
    return  word[::-1] == word
print(is_palindrome("malayalam"))

