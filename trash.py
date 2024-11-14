import random

i = 1
a = (input(f'введи строку номер {i + 1} состоящую из 4 цифр :').split(' '))
a.append(random.randint(0, 99))

# matrix = [(input(f'введи строку номер {i + 1} состоящую из 4 цифр:' ).split(' ')) for i in range(0, 4)]
# print(matrix)
print( a )
