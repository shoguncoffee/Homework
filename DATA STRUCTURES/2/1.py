def Rshift(num, shift):
    return num >> shift

n, s = [int(n) for n in input("Enter number and shiftcount : ").split()]
print(Rshift(n, s))