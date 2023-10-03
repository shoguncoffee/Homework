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
        if self.left is None:
            self.left = node
            
        elif self.right is None: 
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
        yield from list(self.iter('left'))[:0:-1]
        yield from self.iter('right')

    def iter(self, i):
        next = self.root
        while next:
            yield next
            next = getattr(next, i)

    def search(self, item, node=None) -> Node:        
        node = node or self.root
        
        if node.data == item:
            return node
        
        for child in node:
            that_node = self.search(item, child)
            if that_node is not None:
                return that_node
        
             
    def add(self, localroot, item):
        if self.root.data is None:
            left = Node(item, self.root)
            self.root.data = localroot
            self.root.left = left
        else:
            node = self.search(localroot)
            node.add(Node(item, node))

bst = BST()
data = map(str.split, input('Enter Input : ').split(','))
for root, item in data:
    bst.add(root, item)
    
print('Top view :', *bst)