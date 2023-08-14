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
        return ' <- '.join(str(node.data) for node in self)

    def remove(self, index=0):
        self.pop(index)

    def pop(self, index=None):
        index = index or self.size
        prev_node = self.index(index - 1)
        this_node = prev_node.next
        prev_node.next = this_node.next
        self.size -= 1

        return this_node

    def insert(self, data, index=0):
        prev_node = self.index(index - 1)
        new_node = Node(data, prev_node.next)
        prev_node.next = new_node
        self.size += 1

    def append(self, data):
        self.insert(data, self.size)

    def index(self, i):
        if i < self.size:
            if i < 0: 
                return self
            
            return next(
                node for n, node in enumerate(self) if i == n
            )
    
    @property
    def tail(self):
        return self.index(self.size - 1)

    @property
    def head(self):
        return self.index(0)


print(' *** Locomotive ***')
data = input('Enter Input : ').split()

print('Before :', end=' ')
print(*data, sep=' <- ')

l = LinkedList()
seq = map(int, data)

for n in seq:
    if n == 0:
        l.insert(n, 0)
        break

    l.append(n)

for i, n in enumerate(seq, 1):
    l.insert(n, i)
    
print('After :', l)