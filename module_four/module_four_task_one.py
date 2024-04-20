import re

def total_salary(path):
    try:
        with open(path, 'r') as fh:
            content = fh.read()
            find_salary = re.findall('\d+', content)

        money_convert_int = list(map(int, find_salary))
        list_len = len(find_salary)

        total_money = sum(money_convert_int)
        everege_money = int(total_money / list_len)

        return total_money, everege_money
    
    except Exception as e:
        print("Сталася помилка:", e)

result = total_salary("D:\MY_REPO\\first_repo\module_four\\task_one.txt")
print(result)