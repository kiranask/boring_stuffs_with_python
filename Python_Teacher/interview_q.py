s = "Python123"
l = []
for element in s:
    l.append(element)
print(l)
sum = 0
for element in l:
    if element.isdigit():
        sum += int(element)
print(sum)


