data = dict(
    tuple(map(int, i.split('>')))
    for i in input('Enter edges: ').split(',')
)
num = list(data.values())
intersection = sorted(n for n in set(num) if num.count(n) - 1)
reverse_data = {data[k]: k for k in data}

def count(n, *footprint):
    if n not in data:
        return 1
    
    elif n not in footprint:
        return 1 + count(data[n], *footprint, n)

    return 0

def step(next, link: dict):
    while next is not None and next not in intersection:
        yield next
        next = link.get(next)

for n in intersection:
    size = count(n)
    print(f'Node({n}, {size=:})')

branch_in = [
    tuple(step(data[head], data)) 
    for head in intersection
]
branch_out = [
    tuple(step(head, reverse_data))[::-1]
    for head in data if data[head] in intersection
]
branchs = {*branch_in, *branch_out}

pairs = dict(
    sorted(
        pair for branch in branchs 
        for pair in zip(branch[::2], branch[1::2])
    )
)
single = [
    branch[-1] for branch in branchs 
    if len(branch) % 2
]
print(
    *sorted([*single, *pairs.keys()]), 
    *pairs.values(), sep=' -> '
)