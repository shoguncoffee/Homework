def is_plusone_dictionary(d: dict[int, int]):
    l = [i for pair in d.items() for i in pair]
    print(l)
    start, *_, end = l
    print(start, end)
    print(list(range(start, end+1)))
    return l == list(range(start, end+1))

print(is_plusone_dictionary({1:2, 3:4, 5:6, 7:8}))