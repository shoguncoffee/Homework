def buff(i, n):    
    for _ in range(i):
        n = n+2 if n%2 else n-1
        
    return n

data = *map(str.split, input('Enter Input : ').split(',')),

for i, (mode, *_) in enumerate(data):        
    if mode == 'B': 
        height, n, b = 0, 0, 0
        
        for m, *h in data[i-1::-1]:                
            if m == 'S': 
                b += 1
            
            elif m == 'A':
                h = buff(b, int(*h))
                if h > height:
                    height = h
                    n += 1
                
        print(n)