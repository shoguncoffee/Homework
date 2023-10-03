class Node:
    def __init__(self, data, root=None, left=None, right=None):
        self.data = data
        self.root = root
        self.left = left
        self.right = right

    def roots(self):
        root = self.root
        while root:
            yield root
            root = root.root

    def __repr__(self):
        return str(self.data)

    @property
    def is_leaf(self):
        return self.left is self.right is None

    @property
    def is_root(self):
        return self.root is None


class BST:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        yield from self.iter(self.root)

    def iter(self, node):
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
        if self.root is None:
            self.root = Node(item)
        else:
            node = self.search(item)
            new_node = Node(item, node)
            
            if item < node.data:
                node.left = new_node
            else: 
                node.right = new_node

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
check, *data = input('Enter Input : ').split()

for data in map(int, data):
    bst.add(data)

for node in bst:
    print(5 * ' ' * bst.depth(node), node)

num = int(check)
for node, _ in bst.lookup(num):
    if node.data == num:
        if node.is_root:
            print('Root')
        elif node.is_leaf:
            print('Leaf')
        else:
            print('Inner')
        break
else:
    print('Not exist')