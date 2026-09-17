import ast
import runpy


def run_task(filename, capsys):
    runpy.run_path(filename)
    return capsys.readouterr().out.strip().splitlines()


def test_00_distance(capsys):
    result = runpy.run_path('00_distance.py')

    distances = result['distances']

    assert distances['Moscow']['Moscow'] == 0
    assert distances['Moscow']['London'] == distances['London']['Moscow']
    assert distances['Moscow']['Paris'] == distances['Paris']['Moscow']
    assert distances['London']['Paris'] == distances['Paris']['London']


def test_01_circle(capsys):
    output = run_task('01_circle.py', capsys)

    assert output[0] == '5541.7693'
    assert output[1] == 'True'
    assert output[2] == 'False'


def test_02_operations(capsys):
    output = run_task('02_operations.py', capsys)

    assert output[-1] == '25'


def test_03_favorite_movies(capsys):
    output = run_task('03_favorite_movies.py', capsys)

    assert output == [
        'Терминатор',
        'Назад в будущее',
        'Пятый элемент',
        'Чужие',
    ]


def test_04_my_family(capsys):
    output = run_task('04_my_family.py', capsys)

    assert output[0] == 'Рост отца - 172 см'
    assert output[1] == 'Общий рост моей семьи - 989 см'


def test_05_zoo(capsys):
    output = run_task('05_zoo.py', capsys)

    assert output[-2] == 'Лев находится в клетке 1'
    assert output[-1] == 'Жаворонок находится в клетке 7'


def test_06_songs_list(capsys):
    output = run_task('06_songs_list.py', capsys)

    assert output[0] == 'Три песни звучат 14.93 минут'
    assert output[1] == 'А другие три песни звучат 13.49 минут'


def test_07_secret(capsys):
    output = run_task('07_secret.py', capsys)

    assert output[0] == 'в бане веник дороже денег'


def test_08_garden(capsys):
    output = run_task('08_garden.py', capsys)

    all_plants = ast.literal_eval(output[0])
    common_plants = ast.literal_eval(output[1])
    garden_only = ast.literal_eval(output[2])
    meadow_only = ast.literal_eval(output[3])

    assert all_plants == {
        'одуванчик',
        'роза',
        'клевер',
        'гладиолус',
        'ромашка',
        'подсолнух',
        'мак',
    }

    assert common_plants == {
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


def test_09_shopping(capsys):
    result = runpy.run_path('09_shopping.py')

    sweets = result['sweets']

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


def test_10_store(capsys):
    output = run_task('10_store.py', capsys)

    assert 'Лампа - 27 шт, стоимость 1134 руб' in output
    assert 'Стол - 54 шт, стоимость 27860 руб' in output
    assert 'Диван - 3 шт, стоимость 3550 руб' in output
    assert 'Стул - 105 шт, стоимость 10311 руб' in output