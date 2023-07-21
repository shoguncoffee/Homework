print("*** Fun with countdown ***")
num = f' {input("Enter List : ").replace(" ", "  ")} '.replace(' 1 ', '.').replace(' ', '').split('.')

print(num, '->', num[:-1])

lst = []
for n in num[:-1]:
    sub = '1'
    for i in reversed(n):
        if int(i) - int(sub[0]) == 1:
            sub = i + sub
        else: 
            break

    print(repr(n), '->', sub)
    lst.append(sub)

print('=>', [len(lst), lst])