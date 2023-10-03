n, *data = map(int, [
    s for n in input('Enter Input : ').split('/')
    for s in n.split()
])
lenght = len(data)
r = n//2

if lenght != r + 1:
    print('Incorrect Input')
else:
    result = []
    tree = [0] * lenght
    tree[r:] = data
    walk = reversed(tree)

    for i in range(r-1, -1, -1):
        min, max = sorted([next(walk), next(walk)])
        tree[i] = min
        result.append(max - min)

    print(sum(result) + tree[0])