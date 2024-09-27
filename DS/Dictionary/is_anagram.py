"""
Anagram:
Given two strings, check whether two given strings are anagram of each other or not.
An anagram of a string is another string that contains same characters, only the order
of characters can be different. For example, “act” and “tac” are anagram of each other.

How to solve anagram problem,
Take 2 Dic
"""
input_str_1 = "RAM"
input_str_2 = "MAR"
input_str_3 = "allergy"
input_str_4 = "allergic"

print(len(input_str_1))

for i in range(3):
    print (i)
def is_anagram(input_str_1, input_str_2):
    input_str_1= input_str_1.replace(" ","")
    input_str_2 = input_str_2.replace(" ","")
    if len(input_str_1) != len(input_str_2):
        return False
    dict1 = dict()
    dict2 = dict()
    for i in range(len(input_str_1)):
        if input_str_1[i] not in dict1:
            dict1[input_str_1[i]] = 1
        else:
            dict1[input_str_1[i]] += 1
        if input_str_2[i] not in dict2:
            dict2[input_str_2[i]] = 1
        else:
            dict2[input_str_2[i]] += 1
    print("Dict 1", dict1)
    print("Dict2", dict2)
    return dict1 == dict2
print(is_anagram(input_str_1,input_str_2))


