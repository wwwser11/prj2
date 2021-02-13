# 4. Определить, какое число в массиве встречается чаще всего.
import random
print('vvedite diapazon massiiva')
char1 = int(input('min massiva: '))
char2 = int(input('max massiva:'))
user_choice = int(input('vvedite dliny massiva: ' ))
a = [random.randint(char1, char2) for i in range(1, user_choice)]
d = {}
for num, val in enumerate(a, 0):
    value = 0
    for i in a:
        if i == val:
            value += 1
    d[val] = value
print(a)
print(d)
max_key = ''
for val, key in enumerate(sorted(d.keys()), 0):
    if (type(max_key) != int):
        max_key = key
    if max_key < key:
        max_key = key
print(f'Чаще всего встречается {max_key}, {d[max_key]} раз(а)')

