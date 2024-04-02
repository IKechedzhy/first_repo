from datetime import datetime, timedelta

def convert_to_date(date_str):
    return datetime.strptime(date_str, "%Y.%m.%d").date()
    
def is_weekend(date): 
     return date.weekday() >= 5
    
def get_next_birthday(birthday):
    today = datetime.today().date()
    birthday_this_year = birthday.replace(year=today.year)
    
    
    days_difference = (birthday_this_year - today).days


    if days_difference <= 7 and is_weekend(birthday_this_year):
        next_monday = today + timedelta(days=(7 - today.weekday()))
        return next_monday
    else:
        return birthday_this_year
    
def generate_congratulations_list(users):
    congrat = []
    today = datetime.today().date()
    for user in users:
        user_name = user["name"]
        birthday = convert_to_date(user["birthday"])
        next_birthday = get_next_birthday(birthday)
        if 0 <= (next_birthday - today).days <= 7:
            congrat.append({"name": user_name, "birthday": next_birthday.strftime("%Y.%m.%d")})
    return congrat

#Пробую виконати
    
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.04.05"},
    {"name": "Sam Nicolson", "birthday": "1989.08.17"},
    {"name": "Lina Jhonson", "birthday": "1995.11.13"}
]

birthday_congrat = generate_congratulations_list(users)
print(birthday_congrat)
