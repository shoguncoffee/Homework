t = [int(q) for q in input().split(' ')]
h, m = [(e - q) for q, e in zip(t, t[2:])]

if m > 15 or h:
    if h > 6: 
        print(200)
    else: 
        if h > 3:
            h = 3*(h-2) + bool(m)
        print((h + bool(m)) * 10)
else:
    print(0)