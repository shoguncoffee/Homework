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
q1 = Queue()
q2 = Queue()

for command, *value in data:
    if command == 'EN':
        q1.enqueue(*value)

    elif command == 'ES':
        q2.enqueue(*value)

    elif q2.isEmpty():
        if q1.isEmpty():
            print('Empty')
            
        else:
            print(q1.dequeue())

    else:
        print(q2.dequeue())