def odd_or_even(nums, command):
    if command == 'Odd':
        print(sum([n for n in nums if not n % 2 == 0]) * len(nums))
    else:
        print(sum([n for n in nums if n % 2 == 0]) * len(nums))


command = input()
nums = [int(n) for n in input().split()]
odd_or_even(nums, command)
