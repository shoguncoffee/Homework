def length(txt):
    n = -1
    u = ''
    if txt:
        s, *t = txt
        n, j = length(t)
        u = s + '+-'[n%2] + j
        
    return n+1, u

k, l = length(input('Enter Input : '))
v = '~*' if k%2 else '*~'
print(l.replace('+', v[1]).replace('-', v[0]))
print(k)