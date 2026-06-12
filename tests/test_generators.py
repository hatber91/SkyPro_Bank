from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_skyeng(transactions_from_skyeng: list[dict]) -> None:
    """Проверяет фильтрацию транзакций по валюте USD через фикстуру Skyeng"""
    result = list(filter_by_currency(transactions_from_skyeng, "USD"))

    assert result == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


def test_filter_by_currency_usd(transactions: list[dict]) -> None:
    """Проверяет фильтрацию транзакций по валюте USD"""
    result = list(filter_by_currency(transactions, "USD"))

    assert result == [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"},
            },
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300.00",
                "currency": {"name": "USD", "code": "USD"},
            },
        },
    ]


def test_filter_by_currency_without_matches(transactions: list[dict]) -> None:
    """Проверяет случай, когда транзакций с заданной валютой нет"""
    assert list(filter_by_currency(transactions, "EUR")) == []


def test_filter_by_currency_empty_list() -> None:
    """Проверяет работу генератора с пустым списком"""
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_rub(transactions: list[dict]) -> None:
    """Проверяет фильтрацию транзакций по валюте RUB"""
    result = list(filter_by_currency(transactions, "RUB"))

    assert result == [
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency": {"name": "RUB", "code": "RUB"},
            },
        }
    ]


def test_transaction_descriptions(transactions_service: list[dict]) -> None:
    """Проверяет корректный вывод описаний транзакций"""
    result = list(transaction_descriptions(transactions_service))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Оплата услуг",
    ]


def test_transaction_descriptions_empty_list() -> None:
    """Проверяет работу функции с пустым списком"""
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_without_description(transactions: list[dict]) -> None:
    """Проверяет работу функции, если описание отсутствует."""
    transactions = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2},
        {"id": 3, "description": "Оплата услуг"},
    ]

    assert list(transaction_descriptions(transactions)) == [
        "Перевод организации",
        "Оплата услуг",
    ]


def test_card_number_generator_range() -> None:
    """Осуществляет стандартную работу функции в диапазоне от 1 до 5"""
    assert list(card_number_generator(1, 5)) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_card_number_generator_format() -> None:
    """Проверяет корректность форматирования номера карты"""
    assert next(card_number_generator(1234567812345678, 1234567812345678)) == "1234 5678 1234 5678"


def test_card_number_generator_max_value() -> None:
    """Проверяет максимальное значение диапазона."""
    result = next(card_number_generator(9999999999999999, 9999999999999999))
    assert result == "9999 9999 9999 9999"
