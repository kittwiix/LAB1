# -*- coding: utf-8 -*-

import importlib.util
import os


TASK_FILES = [
    '00_distance.py',
    '01_circle.py',
    '02_operations.py',
    '03_favorite_movies.py',
    '04_my_family.py',
    '05_zoo.py',
    '06_songs_list.py',
    '07_secret.py',
    '08_garden.py',
    '09_shopping.py',
    '10_store.py',
]


def take_module(file_path):
    marker = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(marker, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run():
    here = os.path.dirname(os.path.abspath(__file__))
    workdir = os.path.join(here, 'lab_01')
    index = 1
    for name in TASK_FILES:
        path = os.path.join(workdir, name)
        print('---------------- ' + str(index) + ' / 11 ----------------')
        print('файл: ' + name)
        print('----------------------------------------')
        task = take_module(path)
        task.run()
        print()
        index += 1


if __name__ == '__main__':
    run()
