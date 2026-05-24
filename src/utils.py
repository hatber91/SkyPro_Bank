import json
from typing import Any


def get_transactions(file_path: str) -> list[dict[str, Any]]:
    """Функция принимает json файл и возвращает список транзакций"""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    if not isinstance(data, list):
        return []

    return [item for item in data if isinstance(item, dict)]


if __name__ == "__main__":
    my_file_path = "../data/operations.json"
    print(get_transactions(my_file_path))
