# 3. В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.

import random
print('vvedite diapazon massiiva')
char1 = int(input('min massiva: '))
char2 = int(input('max massiva:'))
user_choice = int(input('vvedite dliny massiva: ' ))
a = [random.randint(char1, char2) for i in range(1, user_choice)]
print(a)
min_value = ''
min_index = 0
max_value = ''
max_index = 0
for num, val in enumerate(a, 0):
    if (type(min_value) != int):
        min_value = val
        max_value = val
    if val > max_value:
        max_value = val
        max_index = num
    if val < min_value:
        min_value = val
        min_index = num
a[min_index], a[max_index] = a[max_index], a[min_index]
print(a)
print(max_value, min_value)


