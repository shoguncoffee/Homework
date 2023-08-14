def x():
    yield k := 'hello'
    yield k

print(next(x(), next(x())))