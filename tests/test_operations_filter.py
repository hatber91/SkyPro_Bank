from typing import Any

from src.operations_filter import process_bank_operations, process_bank_search


def test_process_bank_search() -> None:
    """Функция проверяет поиск операций по описанию"""
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод с карты на карту"}
    ]

    result = process_bank_search(data, "перевод")

    assert result == [
        {"id": 1, "description": "Перевод организации"},
        {"id": 3, "description": "Перевод с карты на карту"},
    ]


def test_process_bank_search_empty_result() -> None:
    """Функция проверяет случай, когда операций по поиску нет"""
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"}
    ]

    result = process_bank_search(data, "покупка")

    assert result == []


def test_process_bank_search_without_description() -> None:
    """Функция проверяет, что отсутствие описания не приводит к ошибке"""
    data: list[dict[str, Any]] = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2}
    ]
    result = process_bank_search(data, "перевод")

    assert result == [
        {"id": 1, "description": "Перевод организации"}
    ]


def test_process_bank_operations() -> None:
    """Функция проверяет подсчёт операций по категориям"""
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод организации"},
        {"id": 4, "description": "Перевод с карты на карту"}
    ]
    categories = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод с карты на карту"
    ]
    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Перевод с карты на карту": 1
    }


def test_process_bank_operations_zero_category() -> None:
    """Проверяет категорию, которой нет среди операций."""
    data = [
        {"id": 1, "description": "Перевод организации"}
    ]

    categories = [
        "Перевод организации",
        "Открытие вклада"
    ]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод организации": 1,
        "Открытие вклада": 0
    }
