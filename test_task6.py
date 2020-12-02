# # Задание-1:
# # Дан список, заполненный произвольными целыми числами.
# # Получить новый список, элементы которого будут
# # квадратами элементов исходного списка
# # [1, 2, 4, 0] --> [1, 4, 16, 0]
#
# a = [1, 2, 4, 0]
# b = []
# for number in a:
#     b.append(number ** 2)
# print(b)
#
# # Задание-2:
# # Даны два списка фруктов.
# # Получить список фруктов, присутствующих в обоих исходных списках.
#
#
# fruit1 = ['lemon', 'banana', 'apple']
# fruit2 = ['apple', 'mango', 'orange']
# fruit3 = []
# for fruit in fruit1:
#     if fruit in fruit2:
#         fruit3.append(fruit)
# print(fruit3)
#
# # Задание-3:
# # Дан список, заполненный произвольными числами.
# # Получить список из элементов исходного, удовлетворяющих следующим условиям:
# # + Элемент кратен 3
# # + Элемент положительный
# # + Элемент не кратен 4
#
# numbers1 = [1, 2, 3, 4, 55, 12, 34, 3434, 23, -34, 4, -4, 3, 35454, 9, 99, 7]
# numbers2 = []
# numbers1 = list(set(numbers1))
# for element in numbers1:
#     if (element % 3) == 0:
#         if element > 0:
#             if (element % 4) != 0:
#                 numbers2.append(element)
# print(numbers2)

# Задача - 4
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net),
# te_4_st@test.com - верно указан.
import re
name = input('Ur name: ')
surname = input('Ur surname: ')
email = input('Ur email: ')
name_pattern = '[A-Z]+[a-z]+'
email_pattern = '[a-z0-9_]+@+[a-z]+\.+(ru|org|com)'
match_name = (re.fullmatch(name_pattern, name))
match_surname = (re.fullmatch(name_pattern, surname))
match_email = (re.fullmatch(email_pattern, email))
print('OK' if match_name else "wrong name ;(")
print('OK' if match_surname else "wrong surname ;(")
print('OK' if match_email else "wrong email ;(")