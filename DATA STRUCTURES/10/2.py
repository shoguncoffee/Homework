ls = *map(int, input('Data : ').split()),
m = []

for k, n in enumerate(ls):
    print(k+1, ':', end=' ')
    c = [n]
    
    for i in ls[k::-1]:
        if i < c[-1]:
            c.append(i)

    print(c[::-1])
    m.append(len(c))
     
print('longest increasing subsequence :', max(m))