n,d = 12, 10
temp = 0
for i in range(2, d):
    if n%d == 0:
        print(d)
    elif n%i == 0:
        if i > temp:
            temp = i
print(temp)

