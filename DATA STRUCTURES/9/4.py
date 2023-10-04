ATTR = 'name', 'str', 'int', 'agi'

cending, seq, monkeys = input('Enter Input: ').split('/')
ascending = cending == 'A'
monkey = [
    (name, *map(int, attr)) for name, *attr in
    map(str.split, monkeys.split(','))
]
attrseq = seq.split(',')
index = lambda n: next(i for i, x in enumerate(monkey) if x is n)

def comp(q, e):
    a, s = [
        [item[ATTR.index(i)] for i in attrseq]
        for item in (q, e)
    ]
    if a != s:
        return a > s

    c = index(q) > index(e)
    return c if ascending else not c

def Qsort(arr):
    if not arr: return arr
    
    ltgt = [], []
    arra = iter(arr)
    pv = next(arra)
    
    for n in arra:
        i = comp(n, pv)
        ltgt[i].append(n)
        
    le, gt = map(Qsort, ltgt)
    return (*le, pv, *gt)

if seq:
    u = Qsort(monkey)
    j = u if ascending else u[::-1]
else:
    j = monkey

print('[', end='')
print(*[f'{index(r)}-{r[0]}' for r in j], sep=', ', end=']')