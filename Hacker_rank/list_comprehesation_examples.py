squares = [x**2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


evens = [x for x in range(11) if x % 2 == 0]
print(evens)
# Output: [0, 2, 4, 6, 8, 10]

pairs = [[x, x**2] for x in range(5)]
print(pairs)
# Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]


out = [[i,j, k] for i in range(2) for j in range(2) for k in range(2) if i + j + k !=1]
print(out)