from src import masks

card_number = input('Введите код вашей карты, состоящий из 16 цифр на лицевой стороне пластиковой карты: ')
print(masks.get_mask_card_number(card_number))

account_number = input('Введите номер вашего счёта, состоящий из 20 чисел: ')
print(masks.get_mask_account(account_number))