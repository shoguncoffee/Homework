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


class BST:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        yield from self._iter(self.root)

    def _iter(self, node):
        if node.right is not None:
            yield from self._iter(node.right)

        yield node
        if node.left is not None:
            yield from self._iter(node.left)

    def search(self, item) -> Node:
        n = self.root
        while n:
            next = n.left if item < n.data else n.right
            if next is None:
                return n
            
            n = next
                
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

    def min(self):
        n = self.root
        while n.left:
            n = n.left
        return n

    def max(self):
        n = self.root
        while n.right:
            n = n.right
        return n

bst = BST()
for data in map(int, input('Enter Input : ').split()):
    bst.add(data)

for data in bst:
    print(' ' * 5 * len(list(data.roots())), data)

print('-'*50)
print('Min :', bst.min())
print('Max :', bst.max())