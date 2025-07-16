row = 3
col = 3
num = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
num1 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

sum_matrix = [[0 for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        sum_matrix[i][j] = num[i][j] + num1[i][j]       
print("Sum of matrix")

for i in range(row):
    for j in range(col):
        print(sum_matrix[i][j], end=' ')
    print()