# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.


import random
print('vvedite diapazon massiiva')
char1 = int(input('min massiva: '))
char2 = int(input('max massiva:'))
user_choice = int(input('vvedite dliny massiva: ' ))
a = [random.randint(char1, char2) for i in range(1, user_choice)]
value = ''
index = 0
for i, num in enumerate(a, 0):
    if (type(value) != int) and num < 0:
        value = num
    if num < 0 and num < value:
        value = num
        index = i

print(a)
print(f'значение {value},позиция {index}')