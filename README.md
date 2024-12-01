# ООП Изучение классов
Использование классов и объектов на основе популярной темы e-commerce

Статус: в разработке

## Содержание
- [Технологии](pyproject.toml)
- [Начало работы](src/main.py)
- [Тестирование](tests)


## Разработка
- в модуле category.py реализация класса содержащий информацию о категориях товара, краткой нформации
и количестве товара в категории; магические методы: __ str __
- в модуле product.py реализован класс содержащий информацию о продукте (название, описание, цена, количество)
; магические методы: __ str __, __ add __
- в модуле utils.py реализовано создание объектов класса из переданного файла
- в дериктории tests актуализированы тесты на новый функционал классов


### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
poetry update
```


## Тестирование

Проект покрыт тестатми с помощью библиотеки pytest

Узнать покрытие тестами можно с помощью Code coverage

Наш проект покрыт тестами petest. Чтобы узнать покрытие:
```sh
poetry run pytest --cov
```

### Зачем вы разработали этот проект?
Чтобы показать свою работу над созданием классов на основе ООП и их реализация с основным кодом программы

## To do
- [x] Добавить крутое README
- [ ] Всё переписать
- [ ] ...

## Команда проекта
Оставьте пользователям контакты и инструкции, как связаться с командой разработки.

- [Елена Черноталова](https://t.me/ChashkaChaya813) — хе-хе Возможно надо было ссылку на гит
