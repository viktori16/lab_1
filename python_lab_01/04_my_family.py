#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_family = ['Мама', 'Папа', 'Я', 'Сестра', 'Брат', 'Бабушка']

my_family_height = [
    ['Мама', 165],
    ['Папа', 172],
    ['Я', 168],
    ['Сестра', 159],
    ['Брат', 157],
    ['Бабушка', 168],
]


def get_father_height(family_height):
    return family_height[1][1]


def get_total_height(family_height):
    return sum(person[1] for person in family_height)


def main():
    print('Рост отца -', get_father_height(my_family_height), 'см')
    print(
        'Общий рост моей семьи -',
        get_total_height(my_family_height),
        'см'
    )


if __name__ == '__main__':
    main()