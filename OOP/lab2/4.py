def count_minus(Str: str):
    return sum([int(n) < 0 for n in Str.split()])