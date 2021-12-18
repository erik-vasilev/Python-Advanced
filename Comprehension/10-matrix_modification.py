n = int(input())
matrix = [
    [int(x) for x in input().split()]
    for _ in range(n)
]

line = input()

while not line == 'END':
    command, row, col, value = line.split()
    row, col, value = int(row), int(col), int(value)

    if not (0 <= row < n) or not (0 <= col < n):
        print('Invalid coordinates')
        line = input()
        continue

    if command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

    line = input()

print('\n'.join(' '.join(str(element) for element in row) for row in matrix))
