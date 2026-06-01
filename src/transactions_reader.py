from typing import Any

import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict[Any, Any]]:
    """Функция считывает финансовые операции из CSV файла и возвращает список словарей"""

    transactions = pd.read_csv(file_path, delimiter=";")
    transactions_list = transactions.to_dict(orient="records")

    return transactions_list


def read_transactions_from_excel(file_path: str) -> list[dict[Any, Any]]:
    """Функция считывает финансовые операции из Excel файла и возвращает список словарей"""

    transactions = pd.read_excel(file_path)
    transactions_list = transactions.to_dict(orient="records")

    return transactions_list


# if __name__ == "__main__":
#     print(read_transactions_from_csv("../data/transactions.csv")[:2])
#     print(read_transactions_from_excel("../data/transactions_excel.xlsx")[:2])
