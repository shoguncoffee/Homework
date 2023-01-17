number = sorted(input('Input : ').split())
zero = number.count('0')
number[zero+1:zero+1] = number[:zero]
print(''.join(number[zero:]))