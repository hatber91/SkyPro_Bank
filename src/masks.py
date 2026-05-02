from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер карты, состоящий из 16 чисел и выдаёт в формате маски: XXXX XX** **** XXXX"""
    if len(card_number) == 16:
        card_number = str(card_number)
        card_number_with_stars = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return card_number_with_stars
    elif len(card_number) > 16:
        return f'Вы ввели слишком большое число'
    elif 1 < len(card_number) < 16:
        return f'Вы ввели слишком маленькое число'
    elif len(card_number) == 0:
        return f'Вы не ввели номер карты'



def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер счёта, состоящий из 20 чисел и выдаёт в формате маски: **XXXX"""
    if len(account_number) == 20:
        account_number = str(account_number)
        account_number_with_stars = f"**{account_number[-4:]}"
        return account_number_with_stars
    elif len(account_number) > 20:
        return f'Вы ввели слишком большое число'
    elif 1 < len(account_number) < 20:
        return f'Вы ввели слишком маленькое число'
    elif len(account_number) == 0:
        return f'Вы не ввели номер счёта'
