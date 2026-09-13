# -*- coding: utf-8 -*-

import importlib.util
import os


HERE = os.path.dirname(os.path.abspath(__file__))
TASK_DIR = os.path.join(HERE, '..', 'lab_01')


def load_task(filename):
    path = os.path.join(TASK_DIR, filename)
    marker = filename[:-3]
    spec = importlib.util.spec_from_file_location(marker, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


distance = load_task('00_distance.py')
circle = load_task('01_circle.py')
operations = load_task('02_operations.py')
movies = load_task('03_favorite_movies.py')
family = load_task('04_my_family.py')
zoo = load_task('05_zoo.py')
songs = load_task('06_songs_list.py')
secret = load_task('07_secret.py')
garden = load_task('08_garden.py')
shopping = load_task('09_shopping.py')
store = load_task('10_store.py')


def test_fill_distance_table():
    tiny_map = {
        'A': (0, 0),
        'B': (3, 4),
        'C': (0, 4),
    }
    table = distance.fill_distance_table(tiny_map)
    assert table['A']['B'] == 5
    assert table['B']['A'] == 5
    assert table['A']['C'] == 4
    assert table['C']['B'] == 3
    assert 'A' not in table['A']


def test_moscow_london_paris():
    table = distance.fill_distance_table(distance.sites)
    moscow_london = round(table['Moscow']['London'], 2)
    moscow_paris = round(table['Moscow']['Paris'], 2)
    london_paris = round(table['London']['Paris'], 2)
    assert moscow_london == 145.6
    assert moscow_paris == 130.38
    assert london_paris == 42.43


def test_circle_square():
    area = circle.circle_square(42, 3.1415926)
    assert round(area, 4) == 5541.7693


def test_points_inside_and_outside():
    assert circle.point_is_inside((23, 34), 42) is True
    assert circle.point_is_inside((30, 30), 42) is False
    assert circle.point_is_inside((42, 0), 42) is False


def test_example_and_twenty_five():
    assert operations.example_value() == 9
    assert operations.value_twenty_five() == 25


def test_movie_slices():
    titles = movies.pick_four_titles(movies.my_favorite_movies)
    assert titles == (
        'Терминатор',
        'Назад в будущее',
        'Пятый элемент',
        'Чужие',
    )


def test_family_heights():
    assert family.father_height_cm(family.my_family_height) == 181
    assert family.family_height_cm(family.my_family_height) == 683
    assert len(family.my_family) >= 3
    assert 'папа' in family.my_family


def test_zoo_order_and_cages():
    cages = zoo.place_animals(
        ['lion', 'kangaroo', 'elephant', 'monkey'],
        ['rooster', 'ostrich', 'lark'],
    )
    assert cages == [
        'lion',
        'bear',
        'kangaroo',
        'monkey',
        'rooster',
        'ostrich',
        'lark',
    ]
    assert zoo.cage_of(cages, 'lion') == 1
    assert zoo.cage_of(cages, 'lark') == 7


def test_song_minutes():
    from_list = songs.minutes_from_list(
        songs.violator_songs_list,
        ['Halo', 'Enjoy the Silence', 'Clean'],
    )
    from_dict = songs.minutes_from_dict(
        songs.violator_songs_dict,
        ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'],
    )
    assert from_list == 14.93
    assert from_dict == 13.49


def test_secret_phrase():
    assert secret.read_secret(secret.secret_message) == 'в бане веник дороже денег'


def test_flower_sets():
    garden_set, meadow_set, every_kind, common, only_garden, only_meadow = garden.flower_groups(
        garden.garden,
        garden.meadow,
    )
    assert garden_set == set(garden.garden)
    assert meadow_set == set(garden.meadow)
    assert every_kind == garden_set.union(meadow_set)
    assert common == garden_set.intersection(meadow_set)
    assert only_garden == garden_set.difference(meadow_set)
    assert only_meadow == meadow_set.difference(garden_set)
    assert 'роза' in only_garden
    assert 'мак' in only_meadow
    assert 'ромашка' in common


def test_sweets_two_cheapest():
    offers = shopping.cheap_offers()
    assert offers['печенье'] == [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
    ]
    assert offers['конфеты'] == [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99},
    ]
    assert offers['карамель'] == [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},
    ]
    assert offers['пирожное'] == [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ]


def test_stock_totals():
    totals = store.stock_totals(store.goods, store.store)
    assert totals['Лампа']['pieces'] == 27
    assert totals['Лампа']['money'] == 1134
    assert totals['Стол']['pieces'] == 54
    assert totals['Стол']['money'] == 27860
    assert totals['Диван']['pieces'] == 3
    assert totals['Диван']['money'] == 3550
    assert totals['Стул']['pieces'] == 105
    assert totals['Стул']['money'] == 10311
