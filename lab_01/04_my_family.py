#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

# TODO здесь ваш код

my_family = ['папа', 'мама', 'я', 'брат']
my_family_height = [
    ['папа', 181],
    ['мама', 168],
    ['я', 160],
    ['брат', 174],
]


def father_height_cm(rows):
    for row in rows:
        if row[0] == 'папа':
            return row[1]


def family_height_cm(rows):
    total = 0
    for row in rows:
        total += row[1]
    return total


def run():
    dad = father_height_cm(my_family_height)
    everyone = family_height_cm(my_family_height)
    print(f'Рост отца - {dad} см')
    print(f'Общий рост моей семьи - {everyone} см')


if __name__ == '__main__':
    run()
