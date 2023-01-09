r = (str(i*k) for i in range(999) for k in range(i))
print(max(
    int(q) for q in r if q == q[::-1]
))