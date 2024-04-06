import re

def normalized_phone_numbers(phone_numbers):
    normalized_numbers = []

    for phone_number in phone_numbers:
        normalized_number = re.sub(r'[^\d+]', '', phone_number)

        if normalized_number.startswith('0'):
            normalized_number = '+38' + normalized_number
        
        elif normalized_number.startswith('8'):
            normalized_number = '+3' + normalized_number

        elif normalized_number.startswith('3'):
            normalized_number = '+' + normalized_number

        normalized_numbers.append(normalized_number)

    return normalized_numbers

# перевірка:
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
print(normalized_phone_numbers(raw_numbers))