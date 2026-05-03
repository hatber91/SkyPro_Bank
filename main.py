from src import masks, processing, widget

print("*" * 100)

# card_number = input('Введите код вашей карты, состоящий из 16 цифр на лицевой стороне пластиковой карты:')
card_number = "123456781234567"
print(f"Номер вашей карты: {masks.get_mask_card_number(card_number)}")

# account_number = input('Введите номер вашего счёта, состоящий из 20 чисел: ')
account_number = "123456789012345678901"
print(f"Номер вашей счёта: {masks.get_mask_account(account_number)}")

print("*" * 100)

any_account_number = "Maestro 1596837868705199"

print(widget.mask_account_card(any_account_number))

print("*" * 100)

date_of_entry = "2024-03-11T02:26:18.671407"

print(widget.get_date(date_of_entry))

list_of_dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

state = "EXECUTED"

print(processing.filter_by_state(list_of_dictionaries, state))

print(processing.sort_by_date(list_of_dictionaries, False))
