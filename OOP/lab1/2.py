strs = ''.join(q for q in input() if q.isalpha())
upper = sum(q.islower() for q in strs)
print(upper)
print(len(strs) - upper)