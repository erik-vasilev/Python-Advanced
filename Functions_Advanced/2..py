def round_numbers(numbers):
    return [round(n) for n in numbers]


print(round_numbers([float(n) for n in input().split()]))
