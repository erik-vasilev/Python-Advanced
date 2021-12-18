nums = input().split()
first_set = set()
second_set = set()
for _ in range(int(nums[0])):
    first_set.add(int(input()))

for _ in range(int(nums[1])):
    second_set.add(int(input()))

result = first_set.intersection(second_set)
[print(n) for n in result]
