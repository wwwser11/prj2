# уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
user_numbers = input('Сейчас мы решим уравнение y = kx + b. \nВедите 2 числа(k, b) через запятую: ' )
user_numbers1 = user_numbers.split(',')
equation = f'y = {user_numbers1[0]}x + {user_numbers1[1]}'
x = float(input('Введите х: ' ))
list_equation = equation.split(' ')
b = float(list_equation[-1])
for element in list_equation:
    if "x" in element:
        k = float(element[:-1])
y = k * x + b
print(y)