class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


start, hole = 'FO'
seq = 0, 1, 0, -1
data = input('Enter width, height, and room: ').split()
width, height = map(int, data[:2])
draw = data[-1].split(',')

if [*map(len, draw)] != [width] * height or 'F' not in data[-1]:
    print('Invalid map input.')

else:
    q = Queue()
    past = []
    k = next(n for n, k in enumerate(draw) if start in k)
    h = draw[k].find(start)
    q.enqueue((h, k))
    
    while not q.isEmpty():        
        print('Queue:', q)
        X, Y = q.dequeue()
        
        for a, b in zip(seq, reversed(seq)):
            coor = x, y = X + a, Y + b
            
            if y in range(height) and x in range(width):
                char = draw[y][x]
                
                if char in '_O' and coor not in past:
                    q.enqueue(coor)
                    past.append(coor)
                    
                    if char == hole:
                        print('Found the exit portal.')
                        break
        else:
            continue
        break         
    else:
        print('Cannot reach the exit portal.')