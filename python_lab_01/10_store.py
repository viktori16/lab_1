#!/usr/bin/env python3
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def calculate_store(goods, store):
    result = {}

    for code, products in store.items():
        total_quantity = 0
        total_cost = 0

        for product in products:
            total_quantity += product['quantity']
            total_cost += product['quantity'] * product['price']

        product_name = [
            name for name, product_code in goods.items()
            if product_code == code
        ][0]

        result[product_name] = {
            'quantity': total_quantity,
            'cost': total_cost,
        }

    return result


def main():
    result = calculate_store(goods, store)

    total = sum(product['cost'] for product in result.values())
    print('Общая стоимость товаров -', total)

    for product_name, product in result.items():
        print(
            f"{product_name} - {product['quantity']} шт, "
            f"стоимость {product['cost']} руб"
        )


if __name__ == '__main__':
    main()