s = input().replace(' ', '')
print(up := sum(q.isupper() for q in s))
print(len(s) - up)