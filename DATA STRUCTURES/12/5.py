


class MyInt(int):
    def __sub__(self, other: int):
        return super().__sub__(other//2)

    def getPrime(self):
        primes = []
        for n in range(2, self + 1):
            for p in primes:
                if n % p == 0:
                    break
            else:
                primes.append(n)
            
        return primes
    
    def isPrime(self):
        return self in self.getPrime()

    def showPrime(self):
        primes = [
            str(i) for i in self.getPrime()
        ]
        return ' '.join(primes) if primes else '!!!A prime number is a natural number greater than 1'


print(' *** class MyInt ***')
myints = [
    MyInt(n) for n in input('Enter 2 number : ').split()
]

isPrime = lambda n: f'{n} isPrime : {n.isPrime()}'
showPrime = lambda n: f'Prime number between 2 and {n} : {n.showPrime()}'

for func in isPrime, showPrime:
    for n in myints:
        print(func(n))

print(
    '%d - %d = %d' % (*myints, MyInt.__sub__(*myints))
)