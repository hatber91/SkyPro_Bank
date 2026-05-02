from typing import Union

from src import masks


def mask_account_card(any_account_number: Union[str]) -> Union[str]:
    """Функция принимает информацию о картах или счетах и выводит её в формате маски для одного из типов."""

    letters = "".join(symbol for symbol in any_account_number if symbol.isalpha() or symbol.isspace())
    letters = letters.strip()

    numbers = ""  # создаём строку только с числами

    for sign in any_account_number:
        if sign.isdigit():
            numbers += sign

    if any_account_number == '':
        return f'Вы не внесли данные'
    elif len(any_account_number) > 0:
        if len(numbers) == 16:
            numbers_with_stars = masks.get_mask_card_number(numbers)
            type_and_numbers = f"{letters} {numbers_with_stars}"
            return type_and_numbers
        elif len(numbers) == 20:
            numbers_with_stars = masks.get_mask_account(numbers)
            type_and_numbers = f"{letters} {numbers_with_stars}"
            return type_and_numbers
        elif len(numbers) > 20:
            return f'Номер счёта слишком большой'
        elif 16 < len(numbers) < 20:
            return f'Не хватает цифр в номере счета или номер карты слишком большой'
        elif 1 < len(numbers) < 16:
            return f'Не хватает цифр в номере карты'
        elif len(numbers) == 0:
            return f'Вы не заполнили номер счета или карты!'


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
