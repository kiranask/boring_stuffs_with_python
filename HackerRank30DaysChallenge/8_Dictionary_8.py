import sys

a,b = 10,20

print(a^b)
n = int(input())
name_numbers = [input().split() for _ in range(n)]
print(name_numbers)
test = [['kiran', '2489237498'], ['shravn', '2892398274']]



phone_book = {k:v for k,v in name_numbers}

print(phone_book)
ls = map(lambda x: x.strip(),sys.stdin.readlines())
for name in ls:
    if name in phone_book:
        print('%s=%s' % (name, phone_book[name]))
    else:
        print('Not found')