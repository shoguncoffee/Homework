class Queue:
    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop(0)

    def enqueue(self, *item):
        self.items.append(item)

    def peek(self, i = 0):
        return self.items[i]

    def size(self):
        return len(self.items)

    def __str__(self):
        return ', '.join(self.items) if self.items else 'Empty'

    def isEmpty(self):
        return self.size() == 0


print(' ***Cafe***')
queues = Queue(), Queue()
waiting = []
time = 0

for n, data in enumerate(input('Log : ').split('/'), 1):
    tin, twork = [int(i) for i in data.split(',')]
    order = []
    
    for b in queues:
        t = 0
        while not b.isEmpty():
            N, Tin, Twork = b.peek()
            t += Twork
            finish = time + t
            
            if finish > tin: 
                break
            
            b.dequeue()
            order.append((finish, N))
            waiting.append((finish - Tin, N))
            
    for finish, N in sorted(order): 
        print(f'Time {finish} customer {N} get coffee')
    
    time = tin
    min(queues, 
        key = lambda q: sum(q.peek(i)[-1] for i in range(q.size()))
    ).enqueue(n, tin, twork)


if waiting:
    t, n = max(waiting)
    print('The customer who waited the longest is :', n)
    print(f'The customer waited for {t} minutes')
    
else:
    print('No waiting')