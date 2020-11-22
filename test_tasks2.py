#Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.



input_one = input('Ведите список. Значения необходимо вводить через запятую(, ). : ' )
input_two = input('Ведите список. Значения необходимо вводить через запятую(, ). : ' )
input_split_one = input_one.split(', ')
input_split_two = input_two.split(', ')
for element in input_split_two:
    while element in input_split_one:
        input_split_one.remove(element)
print(input_split_one)
#5, egot, 6, 34, 6, egor
#egor, 5, 54, 4, 6


