from typing import Union


def filter_by_state(list_of_dictionaries: Union[list, dict], state: str = "EXECUTED") -> Union[list]:
    """Функция принимает список словарей и возвращает только словари по определённому ключу"""
    if not isinstance(list_of_dictionaries, list):
        return []

    filtered_list = []

    for item in list_of_dictionaries:
        # пропускаем не-словарные элементы
        if isinstance(item, dict) and item.get("state") == state:
            filtered_list.append(item)

    return filtered_list


def sort_by_date(list_of_dictionaries: Union[list, dict], is_reverse: bool = True) -> Union[list]:
    """Функция сортирует список словарей по дате от большей к меньшей. Можно задать обратный порядок"""
    return sorted(list_of_dictionaries, key=lambda item: item["date"], reverse=is_reverse)
