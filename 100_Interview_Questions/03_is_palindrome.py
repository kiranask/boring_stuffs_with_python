def is_palindrome(s: int):
    if s == 0:
        return True
    str_s = str(s)

    reversed_str_s = str_s[::-1]
    int_reversed_str_s = int(reversed_str_s)
    return s == int_reversed_str_s

def is_palindrome_int(s: int):

    if s < 0:
        return False
    if s == 0:
        return True
    reverse = 0
    while s > 0:
        last = s % 10
        s = s // 10
        reverse = reverse * 10 + last
    return  reverse


print(is_palindrome_int(121))





print(is_palindrome(12111))

