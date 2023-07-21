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

for n, data in enumerate(input('Log : ').split('/'), 1):
    Tin, Twork = [int(i) for i in data.split(',')]
    Tpast, q = min([(
            sum(
                sum(item[:2]) for item in q.items
            ), q
        ) for q in queues], key=lambda x: x[0]
    )
    diff = abs(Tpast - Tin)
    gap = diff if Tin > Tpast else 0
    wait = diff if Tin < Tpast else 0
    q.enqueue(gap, Twork, Tpast, wait, n)

T, N = max(
    max(item[3:] for item in q.items) for q in queues
)
while any(not q.isEmpty() for q in queues):
    *t, _, n = min(queues, 
        key=lambda q: (float('inf'),) if q.isEmpty() else (sum(q.peek()[:3]), q.peek()[-1])
    ).dequeue()
    print(f'Time {sum(t)} customer {n} get coffee')

if T:
    print('The customer who waited the longest is :', N)
    print(f'The customer waited for {T} minutes')
    
else:
    print('No waiting')