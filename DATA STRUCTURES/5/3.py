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

ds = [
    d.split('->') for d in input('Enter Input (L1,L2) : ').split()
]
ls = LinkedList(), LinkedList()

for d, l in zip(ds, ls):
    for data in d:
        l.append(data)

print(f'{"L1":6}: {ls[0]}')
print(f'{"L2":6}: {ls[1]}')

index = ls[0].size
for item in ls[1]:
    ls[0].insert(item.data, index)

print(f'{"Merge":6}: {ls[0]}')