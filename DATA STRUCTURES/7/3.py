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
        else:
            node = self.search(item)
            node.add(Node(item, node))

    def lookup(self, item):
        n = self.root
        while n:
            next = n.left if item < n.data else n.right
            yield n, next
            n = next
               
    def size(self, node):
        return len(list(self.iter(node)))

    def depth(self, node):
        return len(list(node.roots()))


bst = BST()
#d, n = '1 1 2 3 2 3 4 4 5 2 7 5 8 4 6 9 0 -2 -3 -9 -4 0/6'.split('/')
d, n = input('Enter Input : ').split('/')

for data in map(int, d.split()):
    bst.add(data)

for node in bst:
    print(5 * ' ' * bst.depth(node), node)

print('-'*50)
num = int(n)
s = 0

for node, next in bst.lookup(num):
    #print(node, next)
    if node.data <= num:
        s += 1
        
    if node.left and next is node.right:
        s += bst.size(node.left)
        
print(
    s + bool(next and next.data == num),
)