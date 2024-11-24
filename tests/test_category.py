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
