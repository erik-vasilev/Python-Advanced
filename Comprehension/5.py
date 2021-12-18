def is_divisible(number):
    divisible = [num for num in range(2, 11) if number % num == 0]
    return True if divisible else False


start = int(input())
end = int(input())

print([num for num in range(start, end + 1) if is_divisible(num)])
