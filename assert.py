def apply_discount(product: dict, discount: float)->int:  # not needed, but best practice explicit typing
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


def main():
    shoes = {
        'name': 'Fancy Shoes',
        'price': 14900,
    }
    print(apply_discount(shoes, 0.25))  # works,returns 11175

    print(apply_discount(shoes, 2.0))  # breaks with assertion error.


if __name__ == '__main__':
    main()
