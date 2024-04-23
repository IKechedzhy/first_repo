import re
from pathlib import Path

path = Path('module_four') / 'task_one.txt'

def total_salary(path):
    
    try:
        with open(path, 'r', encoding = "utf-8") as fh:
            content = fh.read()
            find_salary = re.findall(r'\d+', content)

        money_convert_int = list(map(int, find_salary))
        list_len = len(find_salary)

        total_money = sum(money_convert_int)
        everege_money = int(total_money / list_len)

        return total_money, everege_money
    
    except Exception as warning:
        print("Сталася помилка:", warning)

print(total_salary(path))
