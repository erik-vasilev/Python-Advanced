n = int(input())
stack = []

for idx in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))

result = []
for i in range(len(stack)):
    result.append(str(stack.pop()))

print(', '.join(result))
