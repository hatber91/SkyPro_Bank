from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер карты, состоящий из 16 чисел и выдаёт в формате маски: XXXX XX** **** XXXX"""
    card_number = str(card_number)
    card_number_with_stars = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return card_number_with_stars


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер счёта, состоящий из 20 чисел и выдаёт в формате маски: **XXXX"""
    account_number = str(account_number)
    account_number_with_stars = f"**{account_number[-4:]}"
    return account_number_with_stars
