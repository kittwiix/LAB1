#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
# Каждый товар может лежать в нескольких местах (партиях) с разной ценой.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# и вывести в формате
#   <товар> - <кол-во> шт, стоимость <сумма> руб

# Пример:
#   Лампа - 27 шт, стоимость 1134 руб

# TODO здесь ваш код


def stock_totals(goods_map, batches):
    totals = {}
    for title, code in goods_map.items():
        pieces = 0
        money = 0
        for batch in batches[code]:
            pieces += batch['quantity']
            money += batch['quantity'] * batch['price']
        totals[title] = {
            'pieces': pieces,
            'money': money,
        }
    return totals


def run():
    totals = stock_totals(goods, store)
    for title in totals:
        pieces = totals[title]['pieces']
        money = totals[title]['money']
        print(f'{title} - {pieces} шт, стоимость {money} руб')


if __name__ == '__main__':
    run()
