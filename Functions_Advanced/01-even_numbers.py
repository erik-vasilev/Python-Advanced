def even_numbers(nums):
    result = list(filter(lambda x: x % 2 == 0, nums))
    return result


nums = [int(n) for n in input().split()]
print(even_numbers(nums))
