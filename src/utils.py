import json
import logging
from typing import Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",
    filemode="w",
    encoding="utf-8",
)

utils_logger = logging.getLogger("utils")


def get_transactions(file_path: str) -> list[dict[str, Any]]:
    """Функция принимает json файл и возвращает список транзакций"""

    utils_logger.info(f"Начато чтение файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []

    except json.JSONDecodeError:
        utils_logger.error(f"Файл пустой или содержит некорректный JSON: {file_path}")
        return []

    if not isinstance(data, list):
        utils_logger.warning("Данные в файле не являются списком")
        return []

    utils_logger.info(f"Файл успешно прочитан. Количество операций: {len(data)}")

    return [item for item in data if isinstance(item, dict)]


if __name__ == "__main__":
    my_file_path = "../data/operations.json"
    print(get_transactions(my_file_path))
