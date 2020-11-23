# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека Функция должна
# возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def name_put (name, age, city):
    return(f'{name}, {age} год(а)/лет, проживает в городе {city}')



name, age, city = map(str, input('vvedi cherez probel name age city : ').split(' '))

print(name_put(name, age, city))
