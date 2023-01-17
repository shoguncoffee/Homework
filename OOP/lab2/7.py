def is_leap(year: int):
    return not year % 4 and bool(year % 100 or not year % 400)

def day_of_year(day: str, month: str, year: str):
    day_of_month = [(31, 30)[m % 2] for m in range(10)]
    day_of_month.insert(7, 31)
    day_of_month[1] = 29 if is_leap(int(year)) else 28
    return int(day) + sum(day_of_month[:int(month) - 1])