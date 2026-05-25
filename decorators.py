from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор для логирования успешного выполнения функции и ошибок"""

    def decorator(function: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                message = f"{function.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as error:
                message = f"{function.__name__} error: {error}. " f"Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)
                raise

        return inner

    return decorator
