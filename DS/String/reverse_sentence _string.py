"""
Write a code to reverse a sentence in python

"""

string ="My name is Kiran Sk"
string_list=list(string.split(" "))
print(string_list)
reverse=""
for i in range ((len(string_list)-1),-1,-1):

    reverse=reverse+ " "+string_list[i]
    print(reverse)

print(reverse)
