heroes = input().split(', ')

inventory = {hero: {} for hero in heroes}

line = input()
while not line == 'End':
    hero, item_name, item_cost = line.split('-')

    if item_name not in inventory[hero]:
        inventory[hero][item_name] = int(item_cost)
    line = input()

for hero in heroes:
    cost = sum(inventory[hero].values())
    item_count = len(inventory[hero])
    print(f'{hero} -> Items: {item_count}, Cost: {cost}')
