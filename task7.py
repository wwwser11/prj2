# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random
print('Введите диапазон массива')
char1 = int(input('Минимально возможное число массива : '))
char2 = int(input('Максимально возможное число массива:'))
user_choice = int(input('Задайте длину массива: ' ))
a = [random.randint(char1, char2) for i in range(1, user_choice)]
first_min_val = ''
second_min_val = ''
# counter = 1
for i, num in enumerate(a, 0):
    if type(first_min_val) != int:
        first_min_val = num
        second_min_val = num
    if first_min_val > num:
        second_min_val = first_min_val
        first_min_val = num
    elif second_min_val > num:
        second_min_val = num

print('Наш массив:', a)
print('Два наименьших числа', first_min_val, second_min_val)
