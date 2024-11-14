# 8. Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
# я добавил возможность ввода матрицы самому или что бы ее делал компьютер полностью(для более быстрой проверки)
import random

user_choice = input('Если хочешь сам ввести матрицу, то нажми Y, если нет, тогда нажми N: ')
if user_choice == 'Y' or user_choice == 'y':
    matrix = [(input(f'Введи строку номер {i + 1} состоящую из 4 цифр, пятое мы добавим сами:' ).split(' ')) for i in range(0, 4)]
elif user_choice == 'N' or user_choice == 'n':
    matrix = [[random.randint(1, 99) for i in range(0, 4)] for i in range(0, 4)]

for line in matrix:
    line.append(random.randint(0,99))
    for i in line:
        print(f'{i:>5}', end='')
    print()

print('-----------------------------------')

for line in matrix:
    l_sum = 0
    for i, item in enumerate(line):
        if i < 4:
            item = int(item)
            l_sum += item
    line.pop(4)
    line.append(l_sum)

for line in matrix:
    for i, item in enumerate(line):
        print(f'{item:>5}', end='')
    print()