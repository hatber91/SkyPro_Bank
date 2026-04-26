from typing import Union

from src import masks


def mask_account_card(any_account_number: Union[str]) -> Union[str]:
    """Функция принмает информацию о картах или счетах и выводит её в формате маски для одного из типов"""

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
