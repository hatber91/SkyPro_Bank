import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(base_card_number: str) -> None:
    """Функция тестирует корректное поведение программы"""
    assert mask_account_card(base_card_number) == "Maestro 1596 83** **** 5199"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_all(value: str, expected: str) -> None:
    """Функция тестирует корректное поведение программы при помощи параметризации"""
    assert mask_account_card(value) == expected


def test_mask_account_card_without_space() -> None:
    """Функция тестирует формат, при котором пользователь при вводе не учёл пробелы"""
    assert mask_account_card("Maestro1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_account_card_less() -> None:
    """Функция тестирует формат, при котором пользователь ввёл не достаточно количество цифр номера карты"""
    assert mask_account_card("Maestro 159683786870519") == "Не хватает цифр в номере карты"


def test_mask_account_card_more() -> None:
    """Функция тестирует формат, при котором пользователь ввёл слишком много цифр номера счёта"""
    assert mask_account_card("Счет 35383033474447895560123546654") == "Номер счёта слишком большой"


def test_mask_account_card_empty_1() -> None:
    """Функция тестирует формат, при котором пользователь не заполнил только номер карты или счёта"""
    assert mask_account_card("Visa") == "Вы не заполнили номер счета или карты!"


def test_mask_account_card_empty_2() -> None:
    """Функция тестирует формат, при котором пользователь при вводе не заполнил поле или оставил пустым"""
    assert mask_account_card("") == "Вы не внесли данные"


def test_get_date(base_date: str) -> None:
    """Функция тестирует корректное поведение программы при вводе даты"""
    assert get_date(base_date) == "11.03.2024"


def test_get_date_empty() -> None:
    """Функция тестирует формат, при котором пользователь не ввёл дату"""
    assert get_date("") == "Вы не ввели дату"


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-12T02:26:18.671407", "12.12.2025"),
        ("2025-12", "Некорректный формат даты"),
        ("202A-1B-1CT02:26:18.671407", "Некорректный формат даты"),
    ],
)
def test_get_date_all(date: str, expected: str) -> None:
    """Функция тестирует разные поведения пользователя при помощи параметризации"""
    assert get_date(date) == expected
