arr = [*map(int, input('Enter Input : ').split())]
more = lambda x: x>=0
arr2 = [*filter(more, arr)]

for n, i in enumerate(arr2):
    for nk, ik in enumerate(arr2[:n]):
        if ik > i: 
            arr2.insert(nk, arr2.pop(n))
            break

r = iter(arr2)
for m, i in enumerate(map(more, arr)):
    print(next(r) if i else arr[m], end=' ')