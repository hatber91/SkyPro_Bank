from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер карты, состоящий из 16 чисел и выдаёт в формате маски: XXXX XX** **** XXXX"""
    if len(card_number) == 0:
        return "Вы не ввели номер карты"
    if 1 <= len(card_number) < 16:
        return "Вы ввели слишком маленькое число"
    if len(card_number) > 16:
        return "Вы ввели слишком большое число"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер счёта, состоящий из 20 чисел и выдаёт в формате маски: **XXXX"""
    if len(account_number) == 0:
        return "Вы не ввели номер счёта"
    if 1 <= len(account_number) < 20:
        return "Вы ввели слишком маленькое число"
    if len(account_number) > 20:
        return "Вы ввели слишком большое число"
    return f"**{account_number[-4:]}"
