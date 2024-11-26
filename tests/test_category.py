def test_category_init(get_category_1, get_category_2):
    assert get_category_1.name == "Смартфоны"
    assert (
        get_category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert len(get_category_1.products) == 2

    assert get_category_1.category_count == 2
    assert get_category_2.category_count == 2
    assert get_category_1.product_count == 3
    assert get_category_2.product_count == 3


def test_add_product(new_product_category):
    assert new_product_category.name == "Смартфоны"
    assert (
        new_product_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert new_product_category.category_count == 1
    assert new_product_category.product_count == 4
    assert new_product_category.products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.',
    ]
