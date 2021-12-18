n = int(input())
elements = set()
for _ in range(n):
    el = input().split()
    for i in el:
        elements.add(i)

[print(name) for name in elements]
