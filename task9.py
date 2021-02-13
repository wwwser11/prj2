# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
line = 5
column = 5
matrix = [[random.randint(-49, 99) for i in range(0, line)] for i in range(0, column)]

for lines in matrix:
    for num in lines:
        print(f'{num:>4}', end='')
    print()
print('---------')
max_ = ''
for j in range(column):
    min_ = matrix[0][j]
    for i in range(line):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]
    if type(max_) != int:
        max_ = min_
    if min_ > max_:
        max_ = min_

print(f'Mаксимальный элемент среди минимальных элементов столбцов матрицы: {max_}')