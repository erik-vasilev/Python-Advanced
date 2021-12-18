from collections import deque

milkshakes = 0

chocolates = [int(n) for n in input().split(', ')]
milk_cups = deque([int(n) for n in input().split(', ')])

while milkshakes < 5 and chocolates and milk_cups:
    last_chocolate = chocolates.pop()
    first_cup = milk_cups.popleft()
    if last_chocolate <= 0 and first_cup <= 0:
        continue
    else:
        if last_chocolate <= 0:
            milk_cups.appendleft(first_cup)
            continue
        if first_cup <= 0:
            chocolates.append(last_chocolate)
            continue

    if last_chocolate == first_cup:
        milkshakes += 1
    else:
        milk_cups.append(first_cup)
        chocolates.append(last_chocolate - 5)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join([str(n) for n in chocolates])}')
else:
    print('Chocolate: empty')
if milk_cups:
    print(f'Milk: {", ".join([str(n) for n in milk_cups])}')
else:
    print('Milk: empty')
