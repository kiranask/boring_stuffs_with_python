from collections import Counter

name = 'KiranSK'

name_dic= Counter(name)
print(name_dic)
for key, value in name_dic.items():
    if value> 1:
        print(key)