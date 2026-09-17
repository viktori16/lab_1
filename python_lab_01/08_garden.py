#!/usr/bin/env python3
# -*- coding: utf-8 -*-

garden = (
    'ромашка',
    'роза',
    'одуванчик',
    'ромашка',
    'гладиолус',
    'подсолнух',
    'роза',
)

meadow = (
    'клевер',
    'одуванчик',
    'ромашка',
    'клевер',
    'мак',
    'одуванчик',
    'ромашка',
)


def get_flowers(garden, meadow):
    garden_set = set(garden)
    meadow_set = set(meadow)

    return (
        garden_set | meadow_set,
        garden_set & meadow_set,
        garden_set - meadow_set,
        meadow_set - garden_set,
    )


def main():
    all_flowers, common, garden_only, meadow_only = get_flowers(
        garden,
        meadow
    )

    print(all_flowers)
    print(common)
    print(garden_only)
    print(meadow_only)


if __name__ == '__main__':
    main()