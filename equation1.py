# уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
equation = 'y = 10x + 105.5'
x = 1

list_equation = equation.split(' ')
print(list_equation)
b = float(list_equation[-1])
for element in list_equation:
    if "x" in element:
        k = float(element[:-1])
y = k * x + b
print(y)