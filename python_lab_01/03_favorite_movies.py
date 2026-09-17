#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'


def get_favorite_movies(movies):
    return [
        movies[0:10],
        movies[-15:],
        movies[12:25],
        movies[35:40],
    ]


def main():
    for movie in get_favorite_movies(my_favorite_movies):
        print(movie)


if __name__ == '__main__':
    main()