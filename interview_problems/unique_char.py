def unique_char(in_str):
    dict = {}
    for char in in_str:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    for value in dict.values():
        if value > 1:
            return False
    return True
print(unique_char("abcdefe"))