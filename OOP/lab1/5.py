generator = (str(i*k) for i in range(999) for k in range(i))
palindrome = (int(q) for q in generator if q == q[::-1])
print(max(palindrome))