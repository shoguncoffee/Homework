class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def _str(self, iter):
        return '->'.join(str(node.data) for node in iter)

    def __iter__(self):
        node = self.head.next
        while node and node.data is not None:
            yield node
            node = node.next

    def __str__(self):
        return self._str(self)

    def reverse(self):
        node = self.tail.prev
        while node and node.data is not None:
            yield node
            node = node.prev
        
    def str_reverse(self):
        return self._str(self.reverse())
    
    def remove(self, data):
        for i, node in enumerate(self):
            if node.data == data:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.size -= 1
                break
        else:
            return None
        return i

    def insert(self, index, data):
        prev_node = self.head if index == 0 else self.index(index - 1)
        next_node = prev_node.next
        
        new_node = Node(data, prev_node, next_node)
        prev_node.next = next_node.prev = new_node
        self.size += 1

    def append(self, data):
        self.insert(self.size, data)

    def index(self, i):
        return next(node for n, node in enumerate(self) if i == n)


l = LinkedList()

for data in input('Enter Input : ').replace(', ', ',').split(','):
    mode, arg = data.split()
    
    if mode == 'A':
        l.append(arg)

    elif mode == 'Ab':
        l.insert(0, arg)
        
    elif mode == 'I':
        index, data = arg.split(':')
        i = int(index)
        
        if 0 <= i <= l.size:
            l.insert(i, data)
            print(f'index = {i} and data = {data}')
        else:
            print('Data cannot be added')

    elif mode == 'R':
        index = l.remove(arg)

        if index is not None:
            print(f'removed : {arg} from index : {index}')
        else:
            print('Not Found!')

    print('linked list :', l)
    print('reverse :', l.str_reverse())