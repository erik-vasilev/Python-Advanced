from collections import deque

quantity_of_food = int(input())
orders = deque(int(i) for i in input().split())
max_number = 0

for i in range(len(orders)):
    if orders[i] > max_number:
        max_number = orders[i]
print(max_number)

while orders:
    next_order = orders[0]
    if next_order <= quantity_of_food:
        quantity_of_food -= orders.popleft()
    else:
        break

orders_left = []
if not orders:
    print('Orders complete')
else:
    while orders:
        orders_left.append(str(orders.popleft()))
    print(f'Orders left: {" ".join(orders_left)}')
