def char_count(Str: str):
    sets = sorted(set(Str), key=lambda s: Str.index(s))
    return {s: Str.count(s) for s in sets}