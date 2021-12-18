from collections import deque


def math_operations(*args, **kwargs):
    numbers = list(args)
    numbers = deque(numbers)
    my_dict = kwargs
    while numbers:
        for i in my_dict:
            if numbers:
                if i == 'a':
                    my_dict[i] = my_dict[i] + numbers.popleft()
                elif i == 's':
                    my_dict[i] = my_dict[i] - numbers.popleft()
                elif i == 'd':
                    try:
                        my_dict[i] = my_dict[i] / numbers.popleft()
                    except ZeroDivisionError:
                        continue
                elif i == 'm':
                    my_dict[i] = my_dict[i] * numbers.popleft()
            else:
                break
    return my_dict


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
