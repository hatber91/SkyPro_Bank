import re
from collections import Counter
from typing import Any


def process_bank_search(data: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    """Функция ищет операции, у которых в описании есть заданная строка"""

    result = []
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    for operation in data:
        description = operation.get("description", "")

        if isinstance(description, str) and pattern.search(description):
            result.append(operation)

    return result


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """Функция считает количество операций по заданным категориям"""

    descriptions = []

    for operation in data:
        description = operation.get("description", "")

        if isinstance(description, str) and description in categories:
            descriptions.append(description)

    counter = Counter(descriptions)

    result = {}

    for category in categories:
        result[category] = counter[category]

    return result
