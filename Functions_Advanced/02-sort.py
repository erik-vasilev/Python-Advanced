def sorted_numbers(nums):
    result = list(sorted(nums))
    return result


nums = [int(n) for n in input().split()]
print(sorted_numbers(nums))
