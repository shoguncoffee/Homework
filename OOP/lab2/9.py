def is_leap(year: int):
    return not year % 4 and bool(year % 100 or not year % 400)

def day_of_year(day: str, month: str, year: str):
    months, years, days = int(month) - 1, int(year), int(day)
    day_of_month = [(31, 30)[m % 2] for m in range(11)]
    day_of_month.insert(7, 31)
    day_of_month[1] = 29 if is_leap(years) else 28
    assert days <= day_of_month[months] and 1 <= months + 1 <= 12 and years >= 0
    return days + sum(day_of_month[:months])

def day_in_year(year: int):
    return 366 if is_leap(year) else 365

def date_diff(*date: str):
    try:
        assert len(date) == 2
        format = [d.split('-') for d in date]
        d1, d2 = [day_of_year(*f) for f in format]
        year = range(*[int(f[-1]) for f in format])
        return d2 - d1 + 1 + sum(day_in_year(y) for y in year)
    except:
        return -1