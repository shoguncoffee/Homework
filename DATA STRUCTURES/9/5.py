def isort(ar):
    for n, i in enumerate(ar):
        for nk, ik in enumerate(ar[:n]):
            if ik > i: 
                ar.insert(nk, ar.pop(n))
                break

def combinations(array, length, prev=[]):
    if len(prev) == length:
        return [prev]
    combs = []
    for i, val in enumerate(array):
        extend = prev.copy()
        extend.append(val)
        combs += combinations(array[i+1:], length, extend)
    return combs

l = {}
a, k = input('Enter Input : ').split('/')
k = *map(int, k.split()),
a = int(a)

for r in range(1, len(k)+1):
    for i in combinations(k, r):
        if sum(i) == a:
            isort(i)
            l.setdefault(len(i), []).append(i)
if l:
    k = list(l)
    isort(k)

    for i in k:
        ls = l[i]
        isort(ls)
        print(*ls, sep='\n')

else:
    print('No Subset')