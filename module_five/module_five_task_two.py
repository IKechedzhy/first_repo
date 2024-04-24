import re

text = """Загальний дохід працівника складається
        з декількох частин: 1000.01 як основний
        дохід, доповнений додатковими надходженнями
         27.45 і 324.00 доларів."""


# def generator_numbers(text):   #"This is function without yeild" 
#     pattern = r"\d*\.?\d+"
#     find_numbers = re.findall(pattern, text)
#     convert_int_numb = list(map(float, find_numbers))
#     return convert_int_numb


def generator_numbers(text): #This is function with yeild

    pattern = r"\d*\.?\d+"
    find_numbers = re.findall(pattern, text)
    for number in find_numbers:
        yield float(number)
     
def sum_profit(text:str, func: callable):
    
    total_salary = sum(func(text))
    return total_salary
    

result = sum_profit(text, generator_numbers)
print(result)
