def even_odd(*args, command):
    if command == 'even':
        return [int(n) for n in args if n % 2 == 0]
    else:
        return [int(n) for n in args if not n % 2 == 0]


print(even_odd(1, 2, 3, 4, 5, 6, command="even"))
