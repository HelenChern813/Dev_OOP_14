class Product:
    """Класс для нейминга продуктов магазина и инфю об их количестве"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация класса для объектов"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
