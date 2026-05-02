from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("1234567812345678") == '1234 56** **** 5678'

def test_get_mask_card_number_less():
    assert get_mask_card_number("123456781234567") == 'Вы ввели слишком маленькое число'

def test_get_mask_card_number_more():
    assert get_mask_card_number("12345678123456789") == 'Вы ввели слишком большое число'

def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == 'Вы не ввели номер карты'


def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == '**7890'

def test_get_mask_account_less():
    assert get_mask_account("1234567890123456789") == 'Вы ввели слишком маленькое число'

def test_get_mask_account_more():
    assert get_mask_account("123456789012345678901") == 'Вы ввели слишком большое число'

def test_get_mask_account_empty():
    assert get_mask_account("") == 'Вы не ввели номер счёта'

