# 2. Во втором массиве сохранить индексы
# четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random
print('vvedite diapazon massiiva')
char1 = int(input('min massiva: '))
char2 = int(input('max massiva:'))
user_choice = int(input('vvedite dliny massiva: ' ))
a = [random.randint(char1, char2) for i in range(1, user_choice)]
b = []
for num, val in enumerate(a, 0):
    if val % 2 == 0:
        b.append(num)
print('Первый массив', a)

print('Второй массив', b)