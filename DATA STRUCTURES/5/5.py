class Node:
    def __init__(self, data=None, next=None):
        super().__init__()
        self.data = data
        self.next = next


class Link:
    def __init__(self):
        super().__init__()
        self.head = Node()

    def _iter(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __iter__(self):
        i = self._iter()
        next(i)
        return i

    @property
    def _tail(self):
        *_, tail = self._iter()
        return tail

    def append(self, node):
        self._tail.next = node


class KeyNode(Node, Link):
    def __init__(self, key):
        super().__init__()
        self.key = key


class KeyList(Link):
    def search(self, key):
        for key_node in self:
            if key_node.key == key:
                return key_node
    
    def next_node(self, key_node):
        if self.search(key_node.key) is None:
            self.append(key_node)
        
    def next_secondary_node(self, key, node):
        a = self.search(key).append(node)
        
    def show_all(self):
        for key_node in self:
            print(key_node.key, ':', end=' ')
            
            for node in key_node:
                print(node.data, end=',')

            print()


l = KeyList()
for i in input('input : ').split(','):
    u, e = i.split(" ")
    
    if u == 'ADN':
        l.next_node(KeyNode(e))
        
    elif u == 'ADSN':
        w, s = e.split('-')
        l.next_secondary_node(w, Node(s))
        
l.show_all()