palindrome = str(input())

reverse = ""

for i in range(len(palindrome)-1,-1,-1):
    print(palindrome[i])
# for i in range(len(palindrome), -1, 1):
#     reverse += palindrome[i]


if reverse == palindrome:
    print("Yes")
else:
    print("No")

