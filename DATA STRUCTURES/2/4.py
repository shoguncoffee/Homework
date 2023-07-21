num = [int(i) for i in input('Enter Your List : ').split()]

if len(num) > 2:
    l = []
    for n1 in num:
        for n2 in num[num.index(n1) + 1:]:
            for n3 in num[num.index(n2) + 1:]:
                d = sorted([n1, n2, n3])
                if sum(d) == 0 and d not in l:
                    l.append(d)
    print(l)
    
else:
    print('Array Input Length Must More Than 2')