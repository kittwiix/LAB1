#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль
# TODO здесь ваш код


# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль
# TODO здесь ваш код


# Уберите слона (elephant) из зоопарка
# и выведите список на консоль
# TODO здесь ваш код


# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
# TODO здесь ваш код


def copy_animals(source):
    copied = []
    for item in source:
        copied.append(item)
    return copied


def place_animals(animals, extra_birds):
    cages = copy_animals(animals)
    cages.insert(1, 'bear')
    for bird in extra_birds:
        cages.append(bird)
    cages.remove('elephant')
    return cages


def cage_of(animals, who):
    number = 0
    for item in animals:
        number += 1
        if item == who:
            return number


def run():
    cages = copy_animals(zoo)

    cages.insert(1, 'bear')
    print(cages)

    for bird in birds:
        cages.append(bird)
    print(cages)

    cages.remove('elephant')
    print(cages)

    print(f'Лев живёт в клетке {cage_of(cages, "lion")}')
    print(f'Жаворонок живёт в клетке {cage_of(cages, "lark")}')


if __name__ == '__main__':
    run()
