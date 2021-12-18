def negatives_vs_positives(nums):
    print(sum([n for n in nums if n < 0]))
    print(sum([n for n in nums if n >= 0]))
    if abs(sum([n for n in nums if n < 0])) > sum([n for n in nums if n >= 0]):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')


nums = [int(n) for n in input().split()]
negatives_vs_positives(nums)
