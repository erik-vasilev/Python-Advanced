sequences = input().split('|')
numbers = [[int(element) for element in seq.split()] for seq in sequences]

numbers.reverse()
numbers = [number for sequence in numbers for number in sequence]

print(' '.join([str(x) for x in numbers]))
