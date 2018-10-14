"""
Find the number of repeated characters in the given String

KiranSK

"""

string="Kiraaan SK"

dic={}

for i in range(len(string)):

    if  string[i] not in dic:

        dic[string[i]] = 1

    else :
        dic[string[i]] += 1

print(dic)
