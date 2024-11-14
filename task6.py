# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
print('Введите диапазон массива')
char1 = int(input('Минимально возможное число массива : '))
char2 = int(input('Максимально возможное число массива:'))
user_choice = int(input('Задайте длину массива: ' ))
a = [random.randint(char1, char2) for i in range(1, user_choice)]
min_value = ''
max_value = ''
min_index = 0
max_index = 0
for i, num in enumerate(a, 0):
    if type(min_value) != int:
        min_value = num
        max_value = num
    if num > max_value:
        max_value = num
        max_index = i
    if num < min_value:
        min_value = num
        min_index = i
sum = 0
if min_index < max_index:
    for i in range(min_index + 1, max_index):
        sum += a[i]
else:
    for i in range(max_index + 1, min_index):
        sum += a[i]
print('Наш массив:', a)
print(f'Индекс минимального числа: {min_index}, Минимальное число: {min_value}')
print(f'Индекс максимального числа: {max_index}, МАксимальное число: {max_value}')
print(f'Сумма между максимальным и минималным числом: {sum}')