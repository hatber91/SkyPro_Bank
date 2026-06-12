from typing import Any
from unittest.mock import Mock, patch

import pandas as pd

from src.transactions_reader import read_transactions_from_csv, read_transactions_from_excel


@patch("src.transactions_reader.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv: Mock) -> None:
    """Функция проверяет считывание транзакций из CSV-файла"""

    test_data = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "amount": 100,
                "currency_code": "RUB",
            },
            {
                "id": 2,
                "state": "CANCELED",
                "amount": 200,
                "currency_code": "USD",
            }
        ]
    )

    mock_read_csv.return_value = test_data

    result: list[dict[str, Any]] = read_transactions_from_csv("test.csv")

    assert result == [
        {
            "id": 1,
            "state": "EXECUTED",
            "amount": 100,
            "currency_code": "RUB",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "amount": 200,
            "currency_code": "USD",
        }
    ]

    mock_read_csv.assert_called_once_with("test.csv", delimiter=";")


@patch("src.transactions_reader.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel: Mock) -> None:
    """Функция проверяет считывание транзакций из Excel-файла"""

    test_data = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "amount": 100,
                "currency_code": "RUB",
            },
            {
                "id": 2,
                "state": "CANCELED",
                "amount": 200,
                "currency_code": "USD",
            },
        ]
    )

    mock_read_excel.return_value = test_data

    result: list[dict[str, Any]] = read_transactions_from_excel("test.xlsx")

    assert result == [
        {
            "id": 1,
            "state": "EXECUTED",
            "amount": 100,
            "currency_code": "RUB",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "amount": 200,
            "currency_code": "USD",
        },
    ]

    mock_read_excel.assert_called_once_with("test.xlsx")
