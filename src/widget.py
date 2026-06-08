from typing import Union

from src import masks


def mask_account_card(any_account_number: Union[str]) -> Union[str]:
    """Функция принимает информацию о картах или счетах и выводит её в формате маски для одного из типов"""

    if any_account_number == "":
        return "Вы не внесли данные"

    letters = "".join(symbol for symbol in any_account_number if symbol.isalpha() or symbol.isspace()).strip()

    numbers = ""  # создаём строку только с числами

    for sign in any_account_number:
        if sign.isdigit():
            numbers += sign

    if len(numbers) == 16:
        numbers_with_stars = masks.get_mask_card_number(numbers)
        return f"{letters} {numbers_with_stars}"

    if len(numbers) == 20:
        numbers_with_stars = masks.get_mask_account(numbers)
        return f"{letters} {numbers_with_stars}"

    if len(numbers) > 20:
        return "Номер счёта слишком большой"

    if 16 < len(numbers) < 20:
        return "Не хватает цифр в номере счета или номер карты слишком большой"

    if 1 <= len(numbers) < 16:
        return "Не хватает цифр в номере карты"

    if len(numbers) == 0:
        return "Вы не заполнили номер счета или карты!"

    return "Вы ввели некорректный номер"


def get_date(date_of_entry: Union[str]) -> Union[str]:
    """Преобразует дату из формата YYYY-MM-DD и тд в формат: ДД.ММ.ГГГГ"""
    if not date_of_entry:
        return "Вы не ввели дату"

    if len(date_of_entry) < 10:
        return "Некорректный формат даты"

    year = date_of_entry[:4]
    month = date_of_entry[5:7]
    day = date_of_entry[8:10]

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return "Некорректный формат даты"

    if date_of_entry[4] != "-" or date_of_entry[7] != "-":
        return "Некорректный формат даты"

    return f"{day}.{month}.{year}"
