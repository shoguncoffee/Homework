class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.next = None
        self.size = 0

    def __iter__(self):
        node = self.next
        while node:
            yield node
            node = node.next

    def __str__(self):
        return ' '.join(str(node.data) for node in self)
        
    def pop(self, index=None):
        index = self.size - 1 if index is None else index
        prev_node = self.index(index - 1)
        next_node = prev_node.next
        prev_node.next = next_node.next
        self.size -= 1

        return next_node.data

    def insert(self, data, index=0):
        prev_node = self.index(index - 1)
        new_node = Node(data, prev_node.next)
        prev_node.next = new_node
        self.size += 1

    def append(self, data):
        self.insert(data, self.size)

    def index(self, i):
        if i < self.size:
            return self if i < 0 else next(
                node for n, node in enumerate(self) if i == n
            )

data, command = input('Enter Input : ').split('/')
data = data.split()
size = len(data)
command = [
    {m: float(n) for m, n in map(str.split, c.split(','))}
    for c in command.split('|')
]
print('-' * 50)

for c in command:
    l = LinkedList()
    for d in data:
        l.append(d)

    R, B = [c[N] for N in 'RB']
    r, b = [int(size * N/100) for N in (R, B)]
    j = int(size * R/50) - size
    remain = size - r
    loop = lambda: zip(range(remain), range(min(r, remain)))
    
    print('Start :', l)
    for _ in range(b):
        l.append(l.pop(0))
    
    print(f'BottomUp {B:.3f} % :', l)
    for i, _ in loop():
        l.insert(l.pop(r + i), 1 + 2*i)

    print(f'Riffle {R:.3f} % :', l)
    
    l2 = LinkedList()
    for i, _ in loop():
        l2.append(l.pop(1 + i))
        
    prev_node = l.index(r - 1)
    l2.index(l2.size - 1).next = prev_node.next
    prev_node.next = l2.next
    l.size += l2.size
    
    print(f'Deriffle {R:.3f} % :', l)
    for _ in range(b):
        l.insert(l.pop())
    
    print(f'Debottomup {B:.3f} % :', l)
    print('-' * 50)