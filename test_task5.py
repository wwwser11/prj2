# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random
player_name = input('Введи имя первого игрока: ')
enemy_name = input('Введи имя второго игрока: ')

player = {'name': player_name, 'health': 100, 'damage': random.randint(0, 50), 'armor': random.triangular(1, 1.5)}
enemy = {'name': enemy_name, 'health': 100, 'damage': random.randint(0, 50), 'armor': random.triangular(1, 1.5)}

def attack_damage(striker, defender):
    real_damage = striker['damage'] / defender['armor']
    return real_damage


def attack(striker, defender):
    health = defender['health']
    #damage = striker['damage']
    #armor = defender['armor']
    if health > 0:
       # health -= float(lambda damage, armor: damage / armor)
        defender['health'] -= attack_damage(striker, defender)
        return 'идем дальше'
    else:
       return f'{ defender["name"] } мертв'


print(attack(player, enemy))
print(player, enemy)
