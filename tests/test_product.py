def test_get_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_creat_new_product(new_product):
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

    new_product.price = 800
    assert new_product.price == 800

    new_product.price = -100
    assert new_product.price == 800
    new_product.price = 0
    assert new_product.price == 800


def test_str_product(product, new_product, product_2, product_3):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."  # 900 000
    assert str(new_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."  # 900 000
    assert str(product_2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."  # 1680000
    assert str(product_3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."  # 434000


def test_add_product(product, product_2, product_3, new_product):
    assert product + product_2 == 2580000.0
    assert product + product_3 == 1334000.0
    assert product + new_product == 1800000.0
    assert product_2 + product_3 == 2114000.0
    assert product_2 + new_product == 2580000.0
    assert product_3 + new_product == 1334000.0
