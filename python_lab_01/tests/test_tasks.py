import importlib


distance = importlib.import_module('00_distance')
circle = importlib.import_module('01_circle')
operations = importlib.import_module('02_operations')
movies = importlib.import_module('03_favorite_movies')
family = importlib.import_module('04_my_family')
zoo = importlib.import_module('05_zoo')
songs = importlib.import_module('06_songs_list')
secret = importlib.import_module('07_secret')
garden = importlib.import_module('08_garden')
shopping = importlib.import_module('09_shopping')
store = importlib.import_module('10_store')


def test_00_distance():
    distances = distance.calculate_distances(distance.sites)

    assert distances['Moscow']['Moscow'] == 0
    assert distances['Moscow']['London'] == distances['London']['Moscow']
    assert distances['Moscow']['Paris'] == distances['Paris']['Moscow']
    assert distances['London']['Paris'] == distances['Paris']['London']


def test_01_circle():
    area = circle.calculate_area(42)

    assert area == 5541.7693
    assert circle.is_inside_circle((23, 34), 42) is True
    assert circle.is_inside_circle((30, 30), 42) is False


def test_02_operations():
    result = operations.calculate_result()

    assert result == 25


def test_03_favorite_movies():
    result = movies.get_favorite_movies(movies.my_favorite_movies)

    assert result == [
        'Терминатор',
        'Назад в будущее',
        'Пятый элемент',
        'Чужие',
    ]


def test_04_my_family():
    father_height = family.get_father_height(family.my_family_height)
    total_height = family.get_total_height(family.my_family_height)

    assert father_height == 172
    assert total_height == 989


def test_05_zoo():
    animals = zoo.prepare_zoo(zoo.zoo.copy(), zoo.birds)

    assert animals.index('lion') + 1 == 1
    assert animals.index('lark') + 1 == 7
    assert 'elephant' not in animals
    assert 'bear' in animals


def test_06_songs_list():
    first_three = songs.calculate_first_three_songs()
    other_three = songs.calculate_other_three_songs()

    assert first_three == 14.93
    assert other_three == 13.49


def test_07_secret():
    result = secret.decode_message(secret.secret_message)

    assert result == 'в бане веник дороже денег'


def test_08_garden():
    all_flowers, common, garden_only, meadow_only = garden.get_flowers(
        garden.garden,
        garden.meadow
    )

    assert all_flowers == {
        'одуванчик',
        'роза',
        'клевер',
        'гладиолус',
        'ромашка',
        'подсолнух',
        'мак',
    }

    assert common == {
        'одуванчик',
        'ромашка',
    }

    assert garden_only == {
        'гладиолус',
        'подсолнух',
        'роза',
    }

    assert meadow_only == {
        'клевер',
        'мак',
    }


def test_09_shopping():
    sweets = shopping.get_sweets()

    assert sweets['печенье'] == [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
    ]

    assert sweets['конфеты'] == [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99},
    ]

    assert sweets['карамель'] == [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},
    ]

    assert sweets['пирожное'] == [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ]


def test_10_store():
    result = store.calculate_store(store.goods, store.store)

    assert result == {
        'Лампа': {'quantity': 27, 'cost': 1134},
        'Стол': {'quantity': 54, 'cost': 27860},
        'Диван': {'quantity': 3, 'cost': 3550},
        'Стул': {'quantity': 105, 'cost': 10311},
    }