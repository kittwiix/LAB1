#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение площади этого круга с точностью до 4-х знаков после запятой


pi = 3.1415926


def circle_square(r, pi_value):
    return pi_value * r ** 2


# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.


def point_is_inside(point, r):
    x = point[0]
    y = point[1]
    from_center = (x ** 2 + y ** 2) ** 0.5
    return from_center < r


# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


def run():
    print(round(circle_square(radius, pi), 4))
    print(point_is_inside(point_1, radius))
    print(point_is_inside(point_2, radius))


if __name__ == '__main__':
    run()
