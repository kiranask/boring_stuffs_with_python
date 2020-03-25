def reverse_string(str, n):
    if n == 0 :
        return str[0]
    return str[n] + reverse_string(str, n -1)


print(reverse_string("abc", 2))