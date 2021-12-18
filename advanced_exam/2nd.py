def shooting(player, direction, matrix):
    row, col = direction
    player_row, player_col = player
    target_hit = []
    while True:
        player_row += row
        player_col += col
        if player_row in range(5) and player_col in range(5):
            if matrix[player_row][player_col] == 'x':
                matrix[player_row][player_col] = '.'
                target_hit = [player_row, player_col]
                break
        else:
            break
    return target_hit, matrix


def find_player(matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == 'A':
                return [row, col]


def check_for_targets(matrix):
    targets = []
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == 'x':
                targets.append([row, col])
    return targets


def move(player, command, matrix):
    direction = command[1]
    steps = int(command[2])
    if direction == 'up':
        if player[0] - steps in range(5):
            if matrix[player[0] - steps][player[1]] == '.':
                matrix[player[0]][player[1]] = '.'
                matrix[player[0] - steps][player[1]] = 'A'
                player = [player[0] - steps, player[1]]
    elif direction == 'down':
        if player[0] + steps in range(5):
            if matrix[player[0] + steps][player[1]] == '.':
                matrix[player[0]][player[1]] = '.'
                matrix[player[0] + steps][player[1]] = 'A'
                player = [player[0] + steps, player[1]]
    elif direction == 'left':
        if player[1] - steps in range(5):
            if matrix[player[0]][player[1] - steps] == '.':
                matrix[player[0]][player[1]] = '.'
                matrix[player[0]][player[1] - steps] = 'A'
                player = [player[0], player[1] - steps]
    elif direction == 'right':
        if player[1] + steps in range(5):
            if matrix[player[0]][player[1] + steps] == '.':
                matrix[player[0]][player[1]] = '.'
                matrix[player[0]][player[1] + steps] = 'A'
                player = [player[0], player[1] + steps]

    return player, matrix


def playing(player, command, matrix):
    direction = command[1]
    hit_target = []
    if direction == 'up' or direction == 'down':
        if direction == 'up':
            target, matrix = shooting(player, [-1, 0], matrix)
            hit_target.append(target)
        elif direction == 'down':
            target, matrix = shooting(player, [1, 0], matrix)
            hit_target.append(target)
    elif direction == 'left' or direction == 'right':
        if direction == 'left':
            target, matrix = shooting(player, [0, -1], matrix)
            hit_target.append(target)
        elif direction == 'right':
            target, matrix = shooting(player, [0, 1], matrix)
            hit_target.append(target)
    return player, matrix, hit_target


shooting_range = [[x for x in input().split()] for _ in range(5)]
player = find_player(shooting_range)
num = int(input())
hit_targets = []

for _ in range(num):
    targets = check_for_targets(shooting_range)
    if not targets:
        break
    info = input().split()
    command = info[0]
    if command == 'move':
        player, shooting_range = move(player, command, shooting_range)
    elif command == 'shoot':
        player, shooting_range, targets_1 = playing(player, command, shooting_range)
        for i in targets_1:
            if len(i) > 0:
                hit_targets.append(i)

if check_for_targets(shooting_range):
    print(f"Training not completed! {len(check_for_targets(shooting_range))} targets left.")
else:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
for i in hit_targets:
    print(i)
