#!/usr/bin/env python3
# -*- coding: utf-8 -*-

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


def calculate_first_three_songs():
    return round(4.9 + 4.20 + 5.83, 3)


def calculate_other_three_songs():
    return round(
        violator_songs_dict['Sweetest Perfection']
        + violator_songs_dict['Policy of Truth']
        + violator_songs_dict['Blue Dress'],
        3
    )


def main():
    print(
        'Три песни звучат',
        calculate_first_three_songs(),
        'минут'
    )

    print(
        'А другие три песни звучат',
        calculate_other_three_songs(),
        'минут'
    )


if __name__ == '__main__':
    main()