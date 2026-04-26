from typing import Union


def filter_by_state(list_of_dictionaries: Union[list, dict], state_value: Union[str]) -> Union[list]:
    """Функция принимает список словарей и возвращает только словари по определённому ключу."""

    filtered_list = []

    for item in list_of_dictionaries:
        if item.get("state") == state_value:
            filtered_list.append(item)

    return filtered_list


def sort_by_date(list_of_dictionaries: Union[list, dict], sorted_by_order=True) -> Union[list]:
    """Функция сортирует список словарей по дате от большей к меньшей. Можно задать обратный порядок."""
    return sorted(list_of_dictionaries, key=lambda item: item["date"], reverse=sorted_by_order)

