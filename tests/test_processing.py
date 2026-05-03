from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(base_list_of_dictionaries: list[dict]) -> None:
    """Функция тестирует словарь по стандартному ключу state, значение которого равно EXECUTED"""
    assert filter_by_state(base_list_of_dictionaries, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_incorrect_state(base_list_of_dictionaries: list[dict]) -> None:
    """Функция тестирует, если ключ state введён не полностью"""
    assert filter_by_state(base_list_of_dictionaries, "EXE") == []


def test_filter_by_state_incorrect_state_is_empty(base_list_of_dictionaries: list[dict]) -> None:
    """Функция тестирует, если ключ state не был заполнен"""
    assert filter_by_state(base_list_of_dictionaries, "") == []


def test_sort_by_date_1(base_list_of_dictionaries: list[dict]) -> None:
    """Функция тестирует сортировку словаря, при исходном параметре is_reverse"""
    assert sort_by_date(base_list_of_dictionaries) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_2(base_list_of_dictionaries: list[dict]) -> None:
    """Функция тестирует сортировку словаря, при изменённом параметре is_reverse"""
    assert sort_by_date(base_list_of_dictionaries, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
