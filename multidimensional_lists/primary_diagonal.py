n = int(input())
matrix = []
result = 0

for row in range(n):
    matrix.append([int(el) for el in input().split()])
    result += matrix[row][row]

print(result)
