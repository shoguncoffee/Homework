def prime(n: int) -> int:
    k = 2*n + 1
    while 1:
        for i in range(2, k):
            if k % i == 0:
                break
        else:
            return k
        k += 1

def show():
    for n, item in enumerate(table, 1):
        debug('#', n, '\t', item, sep='')
        
    debug('-' * 40)

def debug(*args, **kwargs):
    if ok: print(*args, **kwargs)

def notNone(x):
    return x is not None
    
def rehash(text, last=None):
    global table, size, ok
        
    mask = [seq.index(i) for i in table if i is not None]
    size = prime(size)
    table = [None] * size
    
    debug(text)
    ok = False
    if mask:
        hashs(seq[:max(mask) + 1])

    if last is not None:
        hash(last)
    ok = True

def hash(data):
    debug('Add :', data)
    
    if (sum(map(notNone, table)) + 1) / size >= line:
        rehash('****** Data over threshold - Rehash !!! ******')    
        
    for n, q in enumerate(quad):
        h = (data + q) % size
        
        if table[h] is None:
            table[h] = data
            break
        
        print(f'collision number {n+1} at {h}')
    else:
        rehash('****** Max collision - Rehash !!! ******', data)
        
    show()
    
def hashs(arr):
    for data in arr: 
        hash(data)

        
print(' ***** Rehashing *****')

ok = True
vars, data = input('Enter Input : ').split('/')
size, limit, line = map(int, vars.split())

quad = [i**2 for i in range(limit)]
table = [None] * size
line /= 100
seq = *map(int, data.split()),

print('Initial Table :')
show()
hashs(seq)