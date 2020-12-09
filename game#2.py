# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = random.randint(0, 30)
        self.armor = round(random.triangular(1, 1.5), 2)

    # считает на сколько сила удара будет меньше из-за защиты противника
    def _attack_damage(self, enemy):
        real_damage = self.damage / enemy.armor
        return real_damage

    # функция в которой наносится удар
    def _attack(self, enemy):
        enemy.health -= self._attack_damage(enemy)

class Player(Person):
    pass

class Enemy(Person):
    pass


class Game:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def battle(self):
        while self.player.health > 0 and self.enemy.health > 0:
            if self.player.health > 0:
                print(f'{self.player.name} наносит удар')
                self.player._attack(self.enemy)
                if round(self.enemy.health, 2) > 0:
                    print(f'У {self.enemy.name} {round(self.enemy.health, 2)}% жизни')
                else:
                    print(f'{self.enemy.name} труп')
            if self.enemy.health > 0:
                print(f'{self.enemy.name} наносит удар')
                self.enemy._attack(self.player)
                if round(self.player.health, 2) > 0:
                    print(f'У {self.player.name} {round(self.player.health, 2)}% жизни')
                else:
                    print(f'{self.player.name} труп')

        if self.player.health > 0:
            print(f'у {self.player.name} сток жизней {self.player.health} и он выйграл')

        if self.enemy.health > 0:
            print(f'у {self.enemy.name} сток жизней {self.enemy.health} и он выйграл')

player1 = Player(input('input 1st name: '))
player2 = Enemy(input('input 2d name: '))
game = Game(player1, player2)

game.battle()