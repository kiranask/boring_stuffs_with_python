'''
You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if .

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.
Note: The maximum length of this word must be .
Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

SAMPLE INPUT
zzzoooooo
SAMPLE OUTPUT
Yes
Explanation
'''
zoos = str(input())
z_count = 0
o_count = 0
if 'z' and 'o' in zoos:
    for char in zoos:
        if char == 'z':
            z_count +=1
        if char == 'o':
            o_count +=1

if 2*z_count == o_count:
    print("Yes")
else:
    print("No")