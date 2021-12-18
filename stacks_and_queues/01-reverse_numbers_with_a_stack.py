numbers = input().split()
stack_with_numbers = []

while numbers:
    stack_with_numbers.append(numbers.pop())

print(' '.join(stack_with_numbers))
