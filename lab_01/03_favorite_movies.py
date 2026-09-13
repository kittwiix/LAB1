#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться. Переопределять my_favorite_movies нельзя.
# Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код


def pick_four_titles(line):
    first_title = line[0:10]
    last_title = line[42:]
    second_title = line[12:25]
    almost_last_title = line[35:40]
    return first_title, last_title, second_title, almost_last_title


def run():
    first_title, last_title, second_title, almost_last_title = pick_four_titles(my_favorite_movies)
    print(first_title)
    print(last_title)
    print(second_title)
    print(almost_last_title)


if __name__ == '__main__':
    run()
