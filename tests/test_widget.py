from src.widget import mask_account_card, get_date
import pytest

def test_mask_account_card(base_card_number):
    assert mask_account_card(base_card_number) == 'Maestro 1596 83** **** 5199'

@pytest.mark.parametrize('value, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card_all(value, expected):
    assert mask_account_card(value) == expected

def test_mask_account_card_without_space():
    assert mask_account_card('Maestro1596837868705199') == 'Maestro 1596 83** **** 5199'

def test_mask_account_card_less():
    assert mask_account_card('Maestro 159683786870519') == 'Не хватает цифр в номере карты'

def test_mask_account_card_more():
    assert mask_account_card('Счет 35383033474447895560123546654') == 'Номер счёта слишком большой'

def test_mask_account_card_empty_1():
    assert mask_account_card('Visa') == 'Вы не заполнили номер счета или карты!'

def test_mask_account_card_empty_2():
    assert mask_account_card('') == 'Вы не внесли данные'


def test_get_date(base_date):
    assert get_date(base_date) == '11.03.2024'

def test_get_date_empty():
    assert get_date('') == 'Вы не ввели дату'

@pytest.mark.parametrize('date, expected', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-12-12T02:26:18.671407', '12.12.2025'),
    ('2025-12', 'Некорректный формат даты'),
    ('202A-1B-1CT02:26:18.671407', 'Некорректный формат даты'),
])
def test_get_date_all(date, expected):
    assert get_date(date) == expected


