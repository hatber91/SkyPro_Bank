import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/masks.log",
    filemode="w",
    encoding="utf-8",
)

masks_logger = logging.getLogger("masks")


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер карты, состоящий из 16 чисел и выдаёт в формате маски: XXXX XX** **** XXXX"""

    masks_logger.info("Запущена функция get_mask_card_number")

    if len(card_number) == 0:
        masks_logger.error("Пользователь не ввёл номер карты")
        return "Вы не ввели номер карты"

    if 1 <= len(card_number) < 16:
        masks_logger.warning("Пользователь ввёл слишком короткий номер карты")
        return "Вы ввели слишком маленькое число"

    if len(card_number) > 16:
        masks_logger.warning("Пользователь ввёл слишком длинный номер карты")
        return "Вы ввели слишком большое число"

    masks_logger.info("Номер карты успешно замаскирован")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на ввод номер счёта, состоящий из 20 чисел и выдаёт в формате маски: **XXXX"""

    masks_logger.info("Запущена функция get_mask_account")

    if len(account_number) == 0:
        masks_logger.error("Пользователь не ввёл номер счёта")
        return "Вы не ввели номер счёта"

    if 1 <= len(account_number) < 20:
        masks_logger.warning("Пользователь ввёл слишком короткий номер счёта")
        return "Вы ввели слишком маленькое число"

    if len(account_number) > 20:
        masks_logger.warning("Пользователь ввёл слишком длинный номер счёта")
        return "Вы ввели слишком большое число"

    masks_logger.info("Номер счёта успешно замаскирован")
    return f"**{account_number[-4:]}"
