#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def calculate_distances(sites):
    distances = {}

    for city1, coordinates1 in sites.items():
        distances[city1] = {}

        for city2, coordinates2 in sites.items():
            x1, y1 = coordinates1
            x2, y2 = coordinates2

            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[city1][city2] = distance

    return distances


if __name__ == '__main__':
    print(calculate_distances(sites))