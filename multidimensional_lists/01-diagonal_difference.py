def read_matrix(rows):
    matrix = []
    for _ in range(n):
        matrix.append([int(a) for a in input().split()])
    return matrix


n = int(input())
matrix = read_matrix(n)

second_diagonal = 0
main_diagonal = 0
for i in range(n):
    main_diagonal += matrix[i][i]

for i in range(n):
    second_diagonal += matrix[len(matrix) - 1 - i][i]

print(abs(main_diagonal - second_diagonal))
