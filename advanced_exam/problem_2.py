from copy import copy

PLAYER = 'A'
TARGET = 'x'
EMPTY = '.'

directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'right': (0, +1),
    'left': (0, -1)
}


def printing_matrix():
    return [[i for i in input().split()] for i in range(5)]


def player_position(shooting_range):
    for row_index in range(len(shooting_range)):
        if PLAYER in shooting_range[row_index]:
            col_index = shooting_range[row_index].index(PLAYER)
            return row_index, col_index


def targets_count(shooting_range):
    targets = 0
    for i in range(len(shooting_range)):
        for j in range(len(shooting_range[i])):
            if shooting_range[i][j] == TARGET:
                targets += 1
    return targets


def in_range(row, col, shooting_range):
    if row in range(len(shooting_range)) and col in range(len(shooting_range[0])):
        return True
    return False


def iterating_move(shooting_range, direction, steps, player_row, player_col):
    if direction == 'up':
        f = player_row
        cop = copy(player_row)
        for i in range(1, steps + 1):
            f += directions[direction][0] * steps
            if in_range(f, player_col, shooting_range) and shooting_range[player_row - 1][player_col] == EMPTY:
                shooting_range[player_row][player_col] = EMPTY
                player_row -= 1
                shooting_range[player_row][player_col] = PLAYER
                f = cop
            else:
                return shooting_range
    elif direction == 'right':
        c = player_col
        cop = copy(player_col)
        for i in range(1, steps + 1):
            c += directions[direction][1] * steps
            if in_range(player_row, c, shooting_range) and shooting_range[player_row][player_col + 1] == EMPTY:
                shooting_range[player_row][player_col] = EMPTY
                player_col += 1
                shooting_range[player_row][player_col] = PLAYER
                c = cop
            else:
                return shooting_range
    elif direction == 'left':
        c = player_col
        cop = copy(player_col)
        for i in range(1, steps + 1):
            c += directions[direction][1] * steps
            if in_range(player_row, c, shooting_range) and shooting_range[player_row][player_col - 1] == EMPTY:
                shooting_range[player_row][player_col] = EMPTY
                player_col -= 1
                shooting_range[player_row][player_col] = PLAYER
                c = cop
            else:
                return shooting_range
    elif direction == 'down':
        f = player_row
        cop = copy(player_row)
        for i in range(1, steps + 1):
            f += directions[direction][0] * steps
            if in_range(f, player_col, shooting_range) and shooting_range[player_row + 1][player_col] == EMPTY:
                shooting_range[player_row][player_col] = EMPTY
                player_row += 1
                shooting_range[player_row][player_col] = PLAYER
                f = cop
            else:
                return shooting_range
    return shooting_range


def playing_game(shooting_range, n):
    counter = copy(all_targets_count)
    target_positions = []
    player_row = player_position(shooting_range)[0]
    player_col = player_position(shooting_range)[1]
    for i in range(n):
        info = input().split()
        command = info[0]
        direction = info[1]
        if command == 'move':
            steps = int(info[2])
            shooting_range = iterating_move(shooting_range, direction, steps, player_row, player_col)
            player_row = player_position(shooting_range)[0]
            player_col = player_position(shooting_range)[1]
        elif command == 'shoot':
            if direction == 'up':
                cop = copy(player_row)
                while not shooting_range[player_row][player_col] == TARGET:
                    player_row -= 1
                    if in_range(player_row, player_col, shooting_range):
                        if shooting_range[player_row][player_col] == TARGET:
                            counter -= 1
                            shooting_range[player_row][player_col] = EMPTY
                            target_positions.append([player_row, player_col])
                            player_row = cop
                            break
                    else:
                        player_row = cop
                        break
            elif direction == 'down':
                cop = copy(player_row)
                while not shooting_range[player_row][player_col] == TARGET:
                    player_row += 1
                    if in_range(player_row, player_col, shooting_range):
                        if shooting_range[player_row][player_col] == TARGET:
                            counter -= 1
                            shooting_range[player_row][player_col] = EMPTY
                            target_positions.append([player_row, player_col])
                            player_row = cop
                            break
                    else:
                        player_row = cop
                        break
            elif direction == 'left':
                cop = copy(player_col)
                while not shooting_range[player_row][player_col] == TARGET:
                    player_col -= 1
                    if in_range(player_row, player_col, shooting_range):
                        if shooting_range[player_row][player_col] == TARGET:
                            counter -= 1
                            shooting_range[player_row][player_col] = EMPTY
                            target_positions.append([player_row, player_col])
                            player_col = cop
                            break
                    else:
                        player_col = cop
                        break
            elif direction == 'right':
                cop = copy(player_col)
                while not shooting_range[player_row][player_col] == TARGET:
                    player_col += 1
                    if in_range(player_row, player_col, shooting_range):
                        if shooting_range[player_row][player_col] == TARGET:
                            counter -= 1
                            shooting_range[player_row][player_col] = EMPTY
                            target_positions.append([player_row, player_col])
                            player_col = cop
                            break
                    else:
                        player_col = cop
                        break
    return counter, target_positions


shooting_range = printing_matrix()
all_targets_count = targets_count(shooting_range)
counter = copy(all_targets_count)
n = int(input())

targets_left, positions = playing_game(shooting_range, n)

if targets_left > 0:
    print(f'Training not completed! {targets_left} targets left.')
else:
    print(f'Training completed! All {all_targets_count} targets hit.')
for i in positions:
    print(i)
