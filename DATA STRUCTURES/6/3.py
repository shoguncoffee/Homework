n = int(input('Enter Number : '))
bin = [False]*n

def add(digit):
    if bin[digit]:
        bin[digit] = False
        add(digit-1)
    else:
        bin[digit] = True

def f():
    print(*map(int, bin), sep='')
    if not all(bin):
        add(n-1)
        f()

if n > 0:
    f()
elif n == 0:
    print(0)
else:
    print('Only Positive & Zero Number ! ! !')