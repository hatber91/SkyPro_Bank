from typing import Any

from src.generators import filter_by_currency
from src.operations_filter import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.transactions_reader import read_transactions_from_csv, read_transactions_from_excel
from src.utils import get_transactions
from src.widget import get_date, mask_account_card

# def mask_account_or_card(value: str) -> str:
#     """Маскирует карту или счёт"""
#
#     numbers = ""
#
#     for symbol in value:
#         if symbol.isdigit():
#             numbers += symbol
#
#     letters = ""
#
#     for symbol in value:
#         if symbol.isalpha() or symbol.isspace():
#             letters += symbol
#
#     letters = letters.strip()
#
#     if len(numbers) == 16:
#         return f"{letters} {get_mask_card_number(numbers)}"
#
#     if len(numbers) == 20:
#         return f"{letters} {get_mask_account(numbers)}"
#
#     return value


def get_amount_and_currency(operation: dict[str, Any]) -> tuple[str, str]:
    """Возвращает сумму и валюту операции"""

    operation_amount = operation.get("operationAmount")

    if isinstance(operation_amount, dict):
        amount = operation_amount.get("amount", "")
        currency_data = operation_amount.get("currency", {})

        if isinstance(currency_data, dict):
            currency = currency_data.get("code", "")
        else:
            currency = ""

        return str(amount), str(currency)

    amount = operation.get("amount", "")
    currency = operation.get("currency_code", "")

    return str(amount), str(currency)


# def filter_rub_transactions(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
#     """Функция оставляет только рублёвые операции"""
#
#     result = []
#
#     for operation in data:
#         amount, currency = get_amount_and_currency(operation)
#
#         if currency == "RUB":
#             result.append(operation)
#
#     return result


def print_operation(operation: dict[str, Any]) -> None:
    """Функция печатает одну банковскую операцию"""

    date = str(operation.get("date", ""))
    description = str(operation.get("description", ""))

    operation_from = operation.get("from", "")
    operation_to = operation.get("to", "")

    amount, currency = get_amount_and_currency(operation)

    print(f"{get_date(date)} {description}")

    if operation_from and operation_to:
        print(f"{mask_account_card(str(operation_from))} -> {mask_account_card(str(operation_to))}")

    elif operation_to:
        print(mask_account_card(str(operation_to)))

    print(f"Сумма: {amount} {currency}")
    print()


def choose_file_type() -> list[dict[str, Any]]:
    """Позволяет пользователю выбрать источник данных"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_choice = input("Пользователь: ")

    if user_choice == "1":
        print("Для обработки выбран JSON-файл.")
        return get_transactions("data/operations.json")

    if user_choice == "2":
        print("Для обработки выбран CSV-файл.")
        return read_transactions_from_csv("data/transactions.csv")

    if user_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        return read_transactions_from_excel("data/transactions_excel.xlsx")

    print("Выбран неверный пункт меню.")
    return []


def choose_status() -> str:
    """Запрашивает у пользователя корректный статус операции"""

    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        user_status = input("Пользователь: ").upper()

        if user_status in available_statuses:
            print(f'Операции отфильтрованы по статусу "{user_status}"')
            return user_status

        print(f'Статус операции "{user_status}" недоступен.')


def main() -> None:
    """Функция запускает основную логику приложения"""

    transactions = choose_file_type()

    if not transactions:
        print("Не удалось получить транзакции.")
        return

    status = choose_status()
    transactions = filter_by_state(transactions, status)

    sort_answer = input("Отсортировать операции по дате? Да/Нет: ").lower()

    if sort_answer == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").lower()

        if sort_order == "по возрастанию":
            transactions = sort_by_date(transactions, False)
        else:
            transactions = sort_by_date(transactions, True)

    rub_answer = input("Выводить только рублевые транзакции? Да/Нет: ").lower()

    if rub_answer == "да":
        transactions = list(filter_by_currency(transactions, "RUB"))

    search_answer = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()

    if search_answer == "да":
        search_word = input("Введите слово для поиска: ")
        transactions = process_bank_search(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}")
    print()

    for operation in transactions:
        print_operation(operation)


if __name__ == "__main__":
    main()
