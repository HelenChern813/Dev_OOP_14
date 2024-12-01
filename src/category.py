class Category:
    """Класс для реализации категорий в магазине"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализация класса для объектов"""

        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def add_product(self, new_product):
        """Даёт воозможность добавлять новый продукт в список продуктов категории"""

        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        """Выводит список товаров в виде строк в формате: Название продукта, 80 руб. Остаток: 15 шт."""

        product_list = []

        for i in self.__products:
            str_product = f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт."
            product_list.append(str_product)
        return product_list

    def __str__(self):
        count_product_in_category = 0
        for i in self.__products:
            count_product = i.quantity
            count_product_in_category += count_product
        return f"{self.name}, количество продуктов: {count_product_in_category} шт."
