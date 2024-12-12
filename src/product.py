from abc import ABC, abstractmethod


class BaseProduct(ABC):
    '''Базовый класс для продуктов'''

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MixinProduct:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.description}", {self.price}, {self.quantity})'


class Product(BaseProduct, MixinProduct):
    """Класс для нейминга продуктов магазина и инфю об их количестве"""

    def __init__(self, name, description, price, quantity):
        """Инициализация класса для объектов"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.add_price = price * quantity
        super().__init__()

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

    def __str__(self):
        """Реализация функции print"""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Реализация функции сложения"""

        if type(self) == type(other):
            return self.add_price + other.add_price
        else:
            raise TypeError


class Smartphone(Product):
    '''Класс Смартфоны'''

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    '''Класс Газонная трава'''
    def __init__(self, name, description, price, quantity, country, germination_period, color):

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
