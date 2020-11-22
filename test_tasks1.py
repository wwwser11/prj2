# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: [
# ]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

input_words = input('Введите через запятую слова, а фиксики их выровнят и дадут номера :) : ' )
lenght_word = 0
split_words = input_words.split(",")
for word in split_words:
    if len(word) > lenght_word:
        lenght_word = len(word)
# lenght_word=len(max(split_words, key=len))
for index, item in  enumerate(split_words, start=1):
    #print(index, item.rjust(lenght_word))
    print('{}. {}'.format(index, item.rjust(lenght_word)))