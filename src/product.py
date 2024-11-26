class Product:
    """Класс для нейминга продуктов магазина и инфю об их количестве"""

    def __init__(self, name, description, price, quantity):
        """Инициализация класса для объектов"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product):
        """Создает новый объект класса Product из переданного словаря"""

        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Показывает цену продукта без возможности поменять ее"""

        return self.__price

    @price.setter
    def price(self, new_price):
        """Проверяет новую цену, чтобы не продать товар по не корректной цене"""

        if new_price == 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
