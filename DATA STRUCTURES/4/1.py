class Queue:
    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop(0)

    def enqueue(self, item):
        self.items.append(item)

    def __str__(self):
        return ', '.join(self.items) if self.items else 'Empty'

    def isEmpty(self):
        return len(self.items) == 0


data = [word.split() for word in input('Enter Input : ').split(',')]
q = Queue()
c = Queue()

for command, *value in data:
    if command == 'E':
        q.enqueue(*value)
        print(q)
        
    elif q.isEmpty():
        print('Empty')

    else:
        i = q.dequeue()
        c.enqueue(i)
        print(f'{i} <- {q}')

print(f'{c} : {q}')