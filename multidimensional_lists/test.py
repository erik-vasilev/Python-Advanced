rows, columns = [int(el) for el in input().split(', ')]
matrix = []

for row in range(rows):
    matrix.append([int(i) for i in input().split()])
