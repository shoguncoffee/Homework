distant = lambda p1, p2: ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**.5

paths, data = input('Enter a list of points: ').split('/')
start = [*map(float, data.split())]
points = [[*map(float, p)] for p in map(str.split, paths.split(','))]

if start in points:
    points.remove(start)
    
    while points:
        table = {
            distant(point, start): point
            for point in points
        }
        distance = min(table)
        next = table[distance]
        print(f'{start} -> {next} | The distance is {distance:.4f}')
        start = next
        points.remove(start)
else:
    print(start, 'is not in', points)