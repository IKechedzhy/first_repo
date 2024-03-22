from datetime import datetime

date_inp = input("Введіть дату у фоматі РРРР-ММ-ДД: ")

def get_days_from_today(date):
    date_dt = datetime.strptime(date, "%Y-%m-%d")
    today_time = datetime.today()
    new_time = today_time.toordinal() - date_dt.toordinal()
    return new_time

days_fr_today = get_days_from_today(date_inp)
print(f"Різниця між датами дорівнює {days_fr_today} днів")
    