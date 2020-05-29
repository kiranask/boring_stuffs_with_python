matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
r, c  = 3 , 3

print(len(matrix))
for i in range(r):
    for j in range(c):
        print(matrix[i][j])

print("Transpose")

for i in range(c):
    for j in range(r):
        print(matrix[j][i])

matrix=[[matrix[j][i] for i in range(c)] for j in range(r)]

print(matrix)