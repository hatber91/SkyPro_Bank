from src import masks
from src import widget

#card_number = input('Введите код вашей карты, состоящий из 16 цифр на лицевой стороне пластиковой карты: ')
card_number = '1234567812345678'
print(masks.get_mask_card_number(card_number))

#account_number = input('Введите номер вашего счёта, состоящий из 20 чисел: ')
account_number = 12345678901234567890
print(masks.get_mask_account(account_number))

any_account_number = 'Visa Platinum 7000792289606361'

print(widget.mask_account_card(any_account_number))

date_of_entry = "2024-03-11T02:26:18.671407"

print(widget.get_date(date_of_entry))
