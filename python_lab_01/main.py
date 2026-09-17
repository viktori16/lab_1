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


def main():
    print('=== Задание 00. Расстояние между городами ===')
    distances = distance.calculate_distances(distance.sites)
    print(distances)

    print('\n=== Задание 01. Площадь круга ===')
    print(circle.calculate_area(42))
    print(circle.is_inside_circle((23, 34), 42))
    print(circle.is_inside_circle((30, 30), 42))

    print('\n=== Задание 02. Арифметические операции ===')
    print(operations.calculate_result())

    print('\n=== Задание 03. Любимые фильмы ===')
    for movie in movies.get_favorite_movies(movies.my_favorite_movies):
        print(movie)

    print('\n=== Задание 04. Моя семья ===')
    print(
        'Рост отца -',
        family.get_father_height(family.my_family_height),
        'см'
    )
    print(
        'Общий рост моей семьи -',
        family.get_total_height(family.my_family_height),
        'см'
    )

    print('\n=== Задание 05. Зоопарк ===')
    zoo_copy = zoo.prepare_zoo(zoo.zoo.copy(), zoo.birds)
    print(zoo_copy)
    print('Лев находится в клетке', zoo.get_animal_cell(zoo_copy, 'lion'))
    print(
        'Жаворонок находится в клетке',
        zoo.get_animal_cell(zoo_copy, 'lark')
    )

    print('\n=== Задание 06. Список песен ===')
    print(
        'Три песни звучат',
        songs.calculate_first_three_songs(),
        'минут'
    )
    print(
        'А другие три песни звучат',
        songs.calculate_other_three_songs(),
        'минут'
    )

    print('\n=== Задание 07. Секрет ===')
    print(secret.decode_message(secret.secret_message))

    print('\n=== Задание 08. Сад и луг ===')
    all_flowers, common, garden_only, meadow_only = garden.get_flowers(
        garden.garden,
        garden.meadow
    )
    print('Все цветы:', all_flowers)
    print('Общие цветы:', common)
    print('Только в саду:', garden_only)
    print('Только на лугу:', meadow_only)

    print('\n=== Задание 09. Магазины ===')
    print(shopping.get_sweets())

    print('\n=== Задание 10. Магазин ===')
    result = store.calculate_store(store.goods, store.store)

    for product_name, product in result.items():
        print(
            f"{product_name} - {product['quantity']} шт, "
            f"стоимость {product['cost']} руб"
        )


if __name__ == '__main__':
    main()