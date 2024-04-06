from datetime import datetime


def get_days_from_today(date):
    date_dt = datetime.strptime(date, "%Y-%m-%d")
    today_time = datetime.today()
    new_time = today_time.toordinal() - date_dt.toordinal()
    return new_time

while True:

    date_inp = input("Введіть дату у фоматі РРРР-ММ-ДД: ")

    try:

        difference_days = get_days_from_today(date_inp)
        print(f"Різниця між датами дорівнює {difference_days} днів")
        break

    except ValueError:
        print(f"Невірний формат дати(Зразок: РРРР-ММ-ДД)")
    

    