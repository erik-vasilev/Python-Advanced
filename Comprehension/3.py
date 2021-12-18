n = int(input())
nums = []

for _ in range(n):
    nums.extend([int(el) for el in input().split(', ')])

print(nums)
