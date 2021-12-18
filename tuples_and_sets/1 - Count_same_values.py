numbers = tuple([float(el) for el in input().split()])
result = {}

for i in numbers:
    if i not in result:
        result[i] = 0
    result[i] += 1

[print(f'{key} - {value} times') for key, value in result.items()]
