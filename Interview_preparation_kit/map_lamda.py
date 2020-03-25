#

# def square(z):
#     return z*z
numbers = [1,2,3,4,5]
# result = map(square, numbers)
# print(list(result))
result = map(lambda x: x*x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

kiran = "/Kiran SK1"
print(kiran.strip())