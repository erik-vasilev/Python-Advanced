text = list(input())
occurrences = {}

for i in text:
    if i not in occurrences:
        occurrences[i] = 1
    else:
        occurrences[i] += 1

result = dict(sorted(occurrences.items(), key=lambda x: x[0]))

for key, value in result.items():
    print(f'{key}: {value} time/s')
