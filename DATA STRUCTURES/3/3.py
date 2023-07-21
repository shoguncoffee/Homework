data = ''.join(input('Enter Input : ').split())
combo = 0

def check():
    return [
        target for target in dict.fromkeys(char*3 for char in data)
        if target in data
    ]

l = check()
while 1:
    c = check()
    if not c: break
    combo += c != l

    target = c[0]
    data = data.replace(target, '', 1)
    l = c

print(len(data))
print(data[::-1] if data else 'Empty')    

if combo > 0:
    print(f'Combo : {combo+1} ! ! !')