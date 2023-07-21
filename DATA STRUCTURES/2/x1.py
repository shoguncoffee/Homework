num = 4

n = 4*num + 1
background = []

for _ in range(n):
    background.append(['.'] * n)

for start in range(0, 2*num + 1, 2):
    opposite = -start-1
    end = n-start
    
    for shell in start, opposite:
        background[shell][start:end] = ['#'] * (n - 2*start)
        for line in range(start+1, end-1):
            background[line][shell] = '#'

for line in background:
    print(''.join(line))