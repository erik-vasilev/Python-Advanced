categories = input().split(', ')
n = int(input())

bunker = {category: [] for category in categories}

for _ in range(n):
    category, item_name, quality_quantity = input().split(' - ')
    quantity, quality = quality_quantity.split(';')
    quantity, quality = quantity.split(':')[1], quality.split(':')[1]
    quantity, quality = int(quantity), int(quality)

    bunker[category].append({'name': item_name, 'quality': quality, 'quantity': quantity})

    print(category, item_name, quantity, quality)

total_items = sum([item['quantity'] for items in bunker.values() for item in items])
average_quality = sum([item['quality'] for items in bunker.values() for item in items]) / len(categories)

print(f'Count of items: {total_items}')
print(f'Average quality: {average_quality:.2f}')

print('\n'.join(
    f'{category} -> {", ".join(item["item"] for item in bunker[category])}'
    for category in categories
))
