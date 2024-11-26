import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> Any:
    """Читает JSON файл и возвращает PY-объект"""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def create_category_from_json(data: dict) -> list:
    """Создает список объектов класса Category из JSON файла"""

    category_from_file = []
    for category in data:
        category_objects = Category(category["name"], category["description"], category["products"])
        category_from_file.append(category_objects)
    return category_from_file


def create_product_from_json(data: dict) -> list:
    """Создает список объектов класса Product из JSON файла"""

    products_from_file = []
    for category in data:
        for product in category["products"]:
            product_objects = Product(product["name"], product["description"], product["price"], product["quantity"])
            products_from_file.append(product_objects)
    return products_from_file
