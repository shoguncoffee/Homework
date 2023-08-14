n = int(input('Enter Number : '))

def fibo(n):
    return fibo(n-1) + fibo(n-2) if n > 1 else n

print(f'fibo({n}) = {fibo(n)}')