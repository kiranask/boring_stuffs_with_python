def is_anagram(in_s1, in_s2):
    in_s1 = in_s1.replace(" ","")
    in_s2 = in_s2.replace(" ","")

    if len(in_s1) != len(in_s2):
        return False

    for char in in_s1:
        if char in in_s2:
            in_s2 = in_s2.replace(char, "")
    return  len(in_s2) == 0

print(is_anagram("kiran is god","god is kiran"))


