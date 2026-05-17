import pytest

from decorators import log


def test_log_success(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет успешный вывод лога в консоль."""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    add(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет логирование ошибки в консоль."""

    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide error" in captured.out


def test_log_file() -> None:
    """Проверяет запись логов в файл."""
    filename = "test_log.txt"

    @log(filename=filename)
    def add(x: int, y: int) -> int:
        return x + y

    add(1, 2)
    with open(filename, "r", encoding="utf-8") as file:
        result = file.read()
    assert result == "add ok\n"
