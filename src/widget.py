from typing import Union

from src import masks


def mask_account_card(any_account_number: Union[str]) -> Union[str]:
    """Функция принимает информацию о картах или счетах и выводит её в формате маски для одного из типов"""

    letters = "".join(symbol for symbol in any_account_number if symbol.isalpha() or symbol.isspace())

    numbers = ""  # создаём строку только с числами

    for sign in any_account_number:
        if sign.isdigit():
            numbers += sign

    if len(numbers) == 16:
        numbers_with_stars = masks.get_mask_card_number(numbers)
    elif len(numbers) == 20:
        numbers_with_stars = masks.get_mask_account(numbers)

    type_and_numbers = f"{letters} {numbers_with_stars}"
    return type_and_numbers


def get_date(date_of_entry: Union[str]) -> Union[str]:
    """Функция, которая принимает информацию о дате в формате банка и выводит её в удобном для пользователя формате"""
    day = date_of_entry[8:10]
    month = date_of_entry[5:7]
    year = date_of_entry[:4]
    data = f"{day}.{month}.{year}"
    return data
