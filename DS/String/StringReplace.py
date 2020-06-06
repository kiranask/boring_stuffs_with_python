stn="i732847jsdhf"
new=""
for char in stn:
    if char.isnumeric():
        new += new.join(char)
    elif char.isalpha():
        new +=  new.join("+")

print(new)