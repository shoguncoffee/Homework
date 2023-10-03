class Node:
    def __init__(self, data, root=None, left=None, right=None):
        self.data = data
        self.root = root
        self.left = left
        self.right = right
        
    def __iter__(self):
        for child in self.children:
            if child: yield child
    
    @property
    def children(self):
        return self.left, self.right
    
    def roots(self):
        root = self.root
        while root:
            yield root
            root = root.root
            
    def add(self, node):
        condition = node.data < self.data
        
        if self.left is None and condition:
            self.left = node
            
        elif self.right is None and not condition: 
            self.right = node

    def __repr__(self):
        return str(self.data)

    @property
    def is_leaf(self):
        return self.left is self.right is None


class BST:
    def __init__(self):
        self.root = Node(None)

    def __iter__(self):
        yield from self.iter()

    def iter(self, node=None):
        node = node or self.root
        if node.right:
            yield from self.iter(node.right)

        yield node
        if node.left:
            yield from self.iter(node.left)

    def search(self, item) -> Node:
        for node, next in self.lookup(item):
            if next is None:
                return node
            
    def add(self, item):
        if self.root.data is None:
            self.root.data = item
            print('*')
        else:
            node = self.search(item)
            node.add(Node(item, node))

    def lookup(self, item):
        n = self.root
        while n:
            c = item < n.data
            next = n.left if c else n.right
            print('L' if c else 'R', end='')
            if next is None:
                print('*')
                
            yield n, next
            n = next
               
    def size(self, node):
        return len(list(self.iter(node)))

    def depth(self, node):
        return len(list(node.roots()))


bst = BST()
n = input('Enter Input : ').split()

for data in map(int, n):
    bst.add(data)