expression = input()
stack = []
balanced = True

for paren in expression:
    if paren in '[{(':
        stack.append(paren)
    elif paren in ']})':
        if len(stack) == 0:
            balanced = False
            break
        opening_paren = stack.pop()  # guard against empty stack

        if f'{opening_paren}{paren}' not in ['[]', '{}', '()']:
            balanced = False
            break

if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')
