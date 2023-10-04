def isort(l: list, p: list=[]):
    if not p:
        isort(l, [l.pop(0)])
        
    elif not l:
        print('sorted', p, sep='\n')
        
    else:
        n = l.pop(0)
        i = rsort(p, n)
        
        print(f'insert {n} at index {i} :', p, l or '')
        isort(l, p)

def rsort(l: list, n: int, s: list=[]):
    s = s or []
    
    if not l or n < l[0]:
        l[:] = [*s, n, *l]
        return len(s)

    s.append(l.pop(0))    
    return rsort(l, n, s)

isort(
   [*map(int, input('Enter Input : ').split())]
)