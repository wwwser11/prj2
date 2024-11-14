import random

matrix = [[random.randint(1, 15) for i in range(0, 3)] for i in range(0, 3)]
for line in matrix:
    for i in line:
        print(f'{i:>4}', end='')
    print()