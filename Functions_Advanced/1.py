def absolute_values(numbers):
    return [abs(n) for n in numbers]


print(absolute_values([float(n) for n in input().split()]))
