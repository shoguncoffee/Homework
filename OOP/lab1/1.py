r = range(2000//7 + 1, 3200, 7)
print(*[n for n in r if n%5], sep=',')