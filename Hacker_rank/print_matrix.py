matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

value = [number for list in matrix for number in list]
print(value)

for list in matrix:
    for number in list:
        print(number)