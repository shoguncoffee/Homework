start = (2000//7 + 1)*7
iters = range(start, 3200, 7)
generator = (n for n in iters if n%5)
print(*generator, sep=',', end=',')