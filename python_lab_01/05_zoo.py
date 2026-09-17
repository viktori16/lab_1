#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
birds = ['rooster', 'ostrich', 'lark']


def prepare_zoo(zoo, birds):
    zoo.insert(1, 'bear')
    zoo.extend(birds)
    zoo.remove('elephant')
    return zoo


def get_animal_cell(zoo, animal):
    return zoo.index(animal) + 1


def main():
    zoo_copy = zoo.copy()

    zoo_copy.insert(1, 'bear')
    print(zoo_copy)

    zoo_copy.extend(birds)
    print(zoo_copy)

    zoo_copy.remove('elephant')
    print(zoo_copy)

    print('Лев находится в клетке', get_animal_cell(zoo_copy, 'lion'))
    print('Жаворонок находится в клетке', get_animal_cell(zoo_copy, 'lark'))


if __name__ == '__main__':
    main()