from unittest.mock import Mock, patch

from src.external_api import get_amount_in_rub


def test_get_amount_in_rub_for_rub() -> None:
    """Функция проверяет, что транзакция возвращается, без обращения к API"""

    transaction = {"operationAmount": {"amount": "1000.50", "currency": {"code": "RUB"}}}

    result = get_amount_in_rub(transaction)

    assert result == 1000.50


@patch("src.external_api.requests.get")
def test_get_amount_in_rub_for_usd(mock_get: Mock) -> None:
    """Функция проверяет конвертацию USD в RUB через подменный API"""

    transaction = {"operationAmount": {"amount": "10.00", "currency": {"code": "USD"}}}

    mock_response = Mock()
    mock_response.json.return_value = {"result": 900.0}

    mock_get.return_value = mock_response

    result = get_amount_in_rub(transaction)

    assert result == 900.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_get_amount_in_rub_for_eur(mock_get: Mock) -> None:
    """Функция проверяет конвертацию EUR в RUB через подменённый API"""

    transaction = {"operationAmount": {"amount": "10.00", "currency": {"code": "EUR"}}}

    mock_response = Mock()
    mock_response.json.return_value = {"result": 1000.0}

    mock_get.return_value = mock_response

    result = get_amount_in_rub(transaction)

    assert result == 1000.0
    mock_get.assert_called_once()


def test_get_amount_in_rub_for_unknown_currency() -> None:
    """Функция проверяет, что неизвестная валюта возвращает 0.0"""

    transaction = {"operationAmount": {"amount": "10.00", "currency": {"code": "GBP"}}}

    result = get_amount_in_rub(transaction)

    assert result == 0.0
