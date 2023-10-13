print(' ***** Fun with hashing *****')

vars, inp = input('Enter Input : ').split('/')
n, max_col = map(int, vars.split())
data = map(str.split, inp.split(','))

collision = [i**2 for i in range(max_col)]
table = [None] * n

for k, v in data:
    s = sum(map(ord, k))
    
    for i, quad in enumerate(collision):
        h = (s + quad) % n
        if table[h] is None:
            table[h] = k, v
            break
        print(f'collision number {i+1} at {h}')
    else:
        print('Max of collisionChain')
    
    for g, b in enumerate(table,):
        f = b and f"({', '.join(b)})"
        print('#', g, '\t', f, sep='')
    
    print('-' * 27)
    if all(table):
        print('This table is full !!!!!!')
        break