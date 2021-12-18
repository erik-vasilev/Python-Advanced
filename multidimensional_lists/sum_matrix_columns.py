rows, columns = [int(el) for el in input().split(', ')]
matrix = []

for row in range(rows):
    matrix.append([int(i) for i in input().split()])

for col in range(columns):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)
