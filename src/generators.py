from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Функция-генератор принимает на вход список словарей и возвращает итератор,
    который выдаёт транзакции с заданной валютой"""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount")

        if isinstance(operation_amount, dict):
            currency_data = operation_amount.get("currency", {})

            if isinstance(currency_data, dict):
                currency_code = currency_data.get("code", "")

                if currency_code == currency:
                    yield transaction

        elif transaction.get("currency_code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Функция-генератор. Генерирует номера карт в заданном диапазоне"""
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)
        first_numbers = card_number[:4]
        second_numbers = card_number[4:8]
        third_numbers = card_number[8:12]
        fourth_numbers = card_number[12:]
        card_number = f"{first_numbers} {second_numbers} {third_numbers} {fourth_numbers}"
        yield card_number
