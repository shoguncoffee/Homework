s = '#'*10
print(*[s[:-n] for n in range(10)], sep='\n')