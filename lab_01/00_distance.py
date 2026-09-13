#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря


def fill_distance_table(city_map):
    table = {}
    city_names = list(city_map.keys())
    for city in city_names:
        table[city] = {}

    left = 0
    while left < len(city_names):
        right = left + 1
        while right < len(city_names):
            first = city_names[left]
            second = city_names[right]
            x1, y1 = city_map[first]
            x2, y2 = city_map[second]
            length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            table[first][second] = length
            table[second][first] = length
            right += 1
        left += 1
    return table


def run():
    filled = fill_distance_table(sites)
    print(filled)


if __name__ == '__main__':
    run()
