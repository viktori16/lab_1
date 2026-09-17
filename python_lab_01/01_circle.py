#!/usr/bin/env python3
# -*- coding: utf-8 -*-

radius = 42
point_1 = (23, 34)
point_2 = (30, 30)


def calculate_area(radius):
    return round(3.1415926 * radius ** 2, 4)


def is_inside_circle(point, radius):
    distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
    return distance <= radius


def main():
    print(calculate_area(radius))
    print(is_inside_circle(point_1, radius))
    print(is_inside_circle(point_2, radius))


if __name__ == '__main__':
    main()