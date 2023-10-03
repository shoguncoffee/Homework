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
        for next in node.left, node.right:
            if next is not None:
                yield from self._iter(next)

        yield node

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


bst = BST()
for data in map(int, input('Enter input: ').split()):
    bst.add(data)

paths = []
for node in bst:
    if node.is_leaf:
        roots = list(node.roots())
        paths.append(len(roots))

print(f'{len(paths)} path(s)')

for path in sorted(set(paths), reverse=True):
    print(f'{paths.count(path)} path(s) that pass through {path} node(s)')