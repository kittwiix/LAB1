# Лабораторная работа № 1

Репозиторий по дисциплине «Теория алгоритмов» (3 курс, ТвГТУ).
Тема работы: введение в язык программирования Python.

## Что внутри

В каталоге `lab_01` лежат 11 файлов-заданий из архива преподавателя. Имена файлов не менялись.

Верхнеуровневый модуль `run_lab.py` по очереди загружает эти файлы через `importlib.util.spec_from_file_location` и вызывает у каждого функцию `run()`. Печать на консоль выполняется только из `run()`, поэтому обычный импорт модуля ничего не выводит.

Тесты находятся в `tests/` и запускаются через pytest.

```text
LAB1/
├── lab_01/
│   ├── 00_distance.py
│   ├── 01_circle.py
│   ├── 02_operations.py
│   ├── 03_favorite_movies.py
│   ├── 04_my_family.py
│   ├── 05_zoo.py
│   ├── 06_songs_list.py
│   ├── 07_secret.py
│   ├── 08_garden.py
│   ├── 09_shopping.py
│   └── 10_store.py
├── tests/
│   └── test_tasks.py
├── run_lab.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Как запустить одно задание

```bash
cd lab_01
python 00_distance.py
```

Аналогично для остальных файлов: `01_circle.py` … `10_store.py`.

## Как запустить все задания сразу

Из корня репозитория:

```bash
python run_lab.py
```

## Зависимости и тесты

```bash
python -m venv .venv
```

После активации окружения:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Кратко по заданиям

- `00_distance.py` — словарь словарей с евклидовыми расстояниями между городами
- `01_circle.py` — площадь круга и проверка, лежит ли точка внутри
- `02_operations.py` — выражение из чисел 1 2 3 4 5 со значением 25
- `03_favorite_movies.py` — названия фильмов через срезы строки
- `04_my_family.py` — рост отца и сумма ростов семьи
- `05_zoo.py` — вставка, добавление и удаление элементов списка
- `06_songs_list.py` — суммарная длительность песен из списка и из словаря
- `07_secret.py` — расшифровка фразы срезами
- `08_garden.py` — объединение, пересечение и разности множеств
- `09_shopping.py` — вручную собранный словарь двух самых дешёвых предложений
- `10_store.py` — количество и стоимость товаров по партиям

## Полезные ссылки

- https://docs.python.org/3/tutorial/
- https://doka.guide/tools/markdown/
- https://docs.pytest.org/en/latest/
- https://git-scm.com/docs
- https://github.com/still-coding/report_demo
