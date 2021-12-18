contacts = {}
info = input().split('-')
while len(info[0]) > 2:
    if not info[0] in contacts:
        contacts[info[0]] = info[1]
    else:
        contacts[info[0]] = info[1]
    info = input().split('-')

for _ in range(int(info[0])):
    name = input()
    if name not in contacts:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {contacts[name]}')
