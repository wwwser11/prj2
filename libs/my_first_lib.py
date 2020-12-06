# def do_something():
#     return 'I am func'
#
# def more_then_one(num):
#     return num > 1

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil

def make_dirs():
    for i in range(1, 9):
        dir_name = f'dir_{i}'
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
           os.mkdir(dir_path)
        except FileExistsError:
            return "Такая/такие директория/и уже есть!"

def remove_dirs():
    for i in range(1, 9):
        dir_name = f'dir_{i}'
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
           os.rmdir(dir_path)
        except FileNotFoundError:
            return "Такая/такие директория/и уже удалены или не создавались!"

def viewed():
    # return os.listdir(path=".") это отображает все файлы, а необходимо ток папки
    return [i for i in os.listdir() if os.path.isdir(i)]

def f_copy(file_one, file_two):
    shutil.copy(file_one, file_two)

# print(remove_dirs())
# print(make_dirs())
# print(f_copy())
# print(viewed())

def change_dir():
    user_lib = input('В какую папку хочешь перейти? :')
    try:
        os.chdir(user_lib)
        print('\nПерешел')
    except FileNotFoundError:
        print('\nНеверное название папки, такой нет!')

def watcher():
    # user_lib = input('\nКакую папку хочешь посмотреть? :')
    try:
        print(f'\nНаслаждайся просмотренным :\n {os.listdir()}')
    except FileNotFoundError:
        print('\nНеверное название папки, такой нет!')

def remover():
    user_lib = input('\nКакую папку хочешь удалить? :')
    try:
        os.rmdir(user_lib)
        print('\nПапка удалена!')
    except ValueError:
        print('\nНеверное название папки!')
    except OSError:
        print('\nВозможно папка не пустая, проверь, удали, вернись')

def maker():
    user_lib = input('\nКакую папку хочешь создать? :')
    try:
        os.mkdir(user_lib)
        print('\nПапка создана успешно!')
    except OSError:
        print('\nТакая папка уже есть!')

