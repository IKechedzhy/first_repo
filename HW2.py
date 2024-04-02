import random

def get_numbers_ticket(min, max, quantity):
        if min < 1  or max > 1000 or min >= max or quantity < 1 or quantity > 5 :
                return []

        winner_numbers = random.sample(range(min, max + 1), quantity)
        return sorted(winner_numbers)


result = get_numbers_ticket(1, 1000, 5)

print(f"Ващі виграшні номери: {result}")
    