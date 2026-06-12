import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_amount_in_rub(transaction: dict[str, Any]) -> float:
    """Функция берёт транзакцию и переводит её в рубли"""

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        api_key = os.getenv("EXCHANGE_RATES_API_KEY")

        if api_key is None:
            return 0.0

        url = "https://api.apilayer.com/exchangerates_data/convert"

        headers = {"apikey": api_key}

        params = {"from": currency, "to": "RUB", "amount": amount}

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        return float(data["result"])

    return 0.0
