class Queue:
    def __init__(self):
        self.items = []

    def dequeue(self):
        return self.items.pop(0)

    def enqueue(self, item):
        self.items.append(item)

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return len(self.items) == 0


q = Queue()
ed, ei, n = 0, 0, 0
for step in input('input : ').split(','):
    print('Step :', step)
    mode = step[0]

    if mode == 'E':
        for i in range(n, n + int(step[1:])):
            q.enqueue(f'*{i}')
            n += 1
        
        print('Enqueue :', end=' ')

    elif mode == 'D':
        for i in range(int(step[1:])):
            if not q.isEmpty(): 
                q.dequeue()  
            else: 
                ed += 1
                
        print('Dequeue :', end=' ')

    else:
        ei += 1

    print(q)
    print('Error Dequeue :', ed)
    print('Error input :', ei)
    print('-'*20)