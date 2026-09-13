#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код

# Выведите на консоль все виды цветов
# TODO здесь ваш код

# Выведите на консоль те, которые растут и там и там
# TODO здесь ваш код

# Выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код

# Выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код


def flower_groups(garden_tuple, meadow_tuple):
    garden_set = set(garden_tuple)
    meadow_set = set(meadow_tuple)
    every_kind = garden_set.union(meadow_set)
    common = garden_set.intersection(meadow_set)
    only_garden = garden_set.difference(meadow_set)
    only_meadow = meadow_set.difference(garden_set)
    return garden_set, meadow_set, every_kind, common, only_garden, only_meadow


def run():
    garden_set, meadow_set, every_kind, common, only_garden, only_meadow = flower_groups(garden, meadow)
    print(every_kind)
    print(common)
    print(only_garden)
    print(only_meadow)


if __name__ == '__main__':
    run()
