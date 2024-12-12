import pytest


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


def test_smart_cls(smart_product_1):
    assert smart_product_1.name == "Samsung Galaxy S23 Ultra"
    assert smart_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert smart_product_1.price == 180000.0
    assert smart_product_1.quantity == 5
    assert smart_product_1.efficiency == 95.5
    assert smart_product_1.model == "S23 Ultra"
    assert smart_product_1.memory == 256
    assert smart_product_1.color == "Серый"


def test_grass_cls(grass_product_1):
    assert grass_product_1.name == "Газонная трава"
    assert grass_product_1.description == "Элитная трава для газона"
    assert grass_product_1.price == 500.0
    assert grass_product_1.quantity == 20
    assert grass_product_1.country == "Россия"
    assert grass_product_1.germination_period == "7 дней"
    assert grass_product_1.color == "Зеленый"


def test_sum_smrt_grass(smart_product_1, smart_product_2, grass_product_1, grass_product_2):
    assert smart_product_1 + smart_product_2 == 1334000.0
    assert grass_product_1 + grass_product_2 == 16750.0


def test_product_add(smart_product_1, grass_product_1):
    with pytest.raises(TypeError):
        sum_product = smart_product_1 + grass_product_1
        return sum_product
