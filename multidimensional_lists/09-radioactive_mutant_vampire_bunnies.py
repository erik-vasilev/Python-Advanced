rows, cols = [int(x) for x in input().split()]


def read_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(list(input()))
    return matrix


def find_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                return [row, col]


def is_move_valid(row, col):
    return 0 <= row < rows and 0 <= col < cols


def player_move(row, col, direction):
    if direction == 'U':
        potential_row = row - 1
        potential_col = col
    elif direction == 'R':
        potential_col = col + 1
        potential_row = row
    elif direction == 'D':
        potential_row = row + 1
        potential_col = col
    elif direction == 'L':
        potential_col = col - 1
        potential_row = row

    if is_move_valid(potential_row, potential_col):
        matrix[row][col] = '.'
        if matrix[potential_row][potential_col] == 'B':
            return ('dead', potential_row, potential_col)
        matrix[potential_row][potential_col] = 'P'
        return potential_row, potential_col
    matrix[row][col] = '.'
    return 'won', row, col


def get_bunnies_indexes(matrix):
    bunnies = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'B':
                bunnies.append([i, j])

    return bunnies


def mutate_bunny(matrix, row, col, is_dead):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for position in directions:
        potential_row = row + position[0]
        potential_col = col + position[1]
        if is_move_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] == 'P':
                is_dead = True
            matrix[potential_row][potential_col] = 'B'
    return is_dead


def bunnies_mutate(matrix, is_dead):
    bunnies = get_bunnies_indexes(matrix)
    for bunny in bunnies:
        mutate_bunny(matrix, bunny[0], bunny[1], is_dead)


matrix = read_matrix(rows)
player_position = find_player(matrix)
commands = list(input())
is_dead = False

for direction in commands:
    res = player_move(player_position[0], player_position[1], direction)
    is_dead = bunnies_mutate(matrix, is_dead)

    if is_dead:
        for row in matrix:
            print(''.join(row))
        print(f'dead: {res[1]} {res[2]}')
        break

    if res[0] == 'dead':
        for row in matrix:
            print(''.join(row))
        print(f'dead: {res[1]} {res[2]}')
        break
    elif res[0] == 'won':
        for row in matrix:
            print(''.join(row))
        print(f'won: {res[1]} {res[2]}')
        break
    else:
        player_position[0], player_position[1] = res[0], res[1]
