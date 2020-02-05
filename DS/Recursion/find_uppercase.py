# Given a String, find the first uppercase character
# Solve using both an Iterative and Recursive Method.
input_str1 = 'lucidProgrammimg'
input_str2 = 'LucidProgramming'
input_str3= 'lucidprogramming'

def uppercase_iterative(input_str):
    for char in input_str:
        if char.isupper():
            return char
    return "No Uppercase character found"

def uppercase_recursive(input_str, index=0):
    if input_str[index].isupper():
        return input_str[index]
    if index == len(input_str)-1:
        return "No Uppercase character found"
    uppercase_recursive(input_str, index+1)

print(uppercase_iterative(input_str1))
print(uppercase_iterative(input_str2))
print(uppercase_iterative(input_str3))

print(uppercase_iterative(input_str1))
print(uppercase_iterative(input_str2))
print(uppercase_iterative(input_str3))