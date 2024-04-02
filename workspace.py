from datetime import datetime, timedelta

def convert_to_date(date_str):
    return datetime.strptime(date_str, "%Y.%m.%d").date()

def is_weekend(date):
    return date.weekday() >= 5

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        user_name = user["name"]
        birthday = convert_to_date(user["birthday"])
        
        if not birthday:
            print(f"Некоректна дата народження для користувача {user_name}. Пропускаю.")
            continue

        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (next_birthday - today).days
        if 0 < days_until_birthday <= 7:
            if is_weekend(next_birthday):
                next_birthday += timedelta(days=(7 - next_birthday.weekday()))

            upcoming_birthdays.append({"name": user_name, "congratulation_date": next_birthday.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.04.5"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)