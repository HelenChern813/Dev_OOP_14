from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс для продуктов"""

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass
