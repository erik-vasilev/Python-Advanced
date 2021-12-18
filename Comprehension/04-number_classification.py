nums = [int(n) for n in input().split(', ')]

positive = [x for x in nums if x >= 0]
negative = [x for x in nums if x < 0]
even = [x for x in nums if x % 2 == 0]
odd = [x for x in nums if not x % 2 == 0]

print('Positive:', ', '.join([str(x) for x in positive]))
print('Negative:', ', '.join([str(x) for x in negative]))
print('Even:', ', '.join([str(x) for x in even]))
print('Odd:', ', '.join([str(x) for x in odd]))
