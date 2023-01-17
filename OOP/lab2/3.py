def delete_minus(x: list[list[int]]):
    return [[n for n in l if n > 0] for l in x]