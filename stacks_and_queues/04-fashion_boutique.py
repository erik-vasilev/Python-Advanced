box = list(map(int, input().split()))
capacity = int(input())
current_capacity = capacity
counter_racks = 1
while len(box) > 0:
    current_v_clothes = box.pop()

    if current_v_clothes <= current_capacity:
        current_capacity -= current_v_clothes
    else:
        counter_racks += 1
        current_capacity = capacity
        current_capacity -= current_v_clothes

print(counter_racks)
