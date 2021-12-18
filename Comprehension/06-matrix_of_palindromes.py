n, m = input().split()
n, m = int(n), int(m)

base = ord('a')


def generate_element(row, col):
    first_letter = chr(row + base)
    middle_letter = chr(row + col + base)
    return f'{first_letter}{middle_letter}{first_letter}'


matrix = [[generate_element(row, col) for col in range(m)] for row in range(n)]
print('\n'.join(' '.join([str(element) for element in row]) for row in matrix))
