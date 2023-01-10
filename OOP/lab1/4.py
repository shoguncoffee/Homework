number = input('Input : ')
answer = sum(int(number*i) for i in range(1, 5))
print('Output :', answer)