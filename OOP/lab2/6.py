def add2list(*lst: list[int]):
    return [sum(n) for n in zip(*lst)]