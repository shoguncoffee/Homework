class Node:
    attr = 'left', 'right'
    
    def __init__(self, data, root=None, left=None, right=None):
        self.data = data
        self.root = root
        self.left = left
        self.right = right

    def __ge__(self, other):
        return self.data >= other.data

    def __bool__(self):
        return self.data is not None

    def __iter__(self):
        for child in self.children:
            if child: yield child
    
    @property
    def children(self):
        return self.left, self.right
    
    def roots(self):
        root: Node = self.root
        while root:
            yield root
            root = root.root

    def setchild(self, node, p: int):
        self.__setattr__(Node.attr[p], node)
        
        if node is not None:
            node.root = self

    def replace(self, old, new):
        i = self.children.index(old)
        self.setchild(new, i)
            
    def add(self, node):
        self.setchild(node, node >= self)
        
    def __getitem__(self, key):
        return self.children[key]

    def __repr__(self):
        return str(self.data)

    @property
    def is_leaf(self):
        return self.left is self.right is None


class AVL:
    def __init__(self):
        self.setroot()

    def __iter__(self):
        yield from self.iter(self.root)

    def iter(self, node, depth=0):
        yield node, depth
        
        if node and not node.is_leaf:
            for child in node.children:
                yield from self.iter(child, depth+1)
            
    def setroot(self, node=None):
        node = node or Node(None)
        self.root = node
        node.root = None
 
    def add(self, item):
        if self.unset:
            self.root.data = item
        else:
            *_, node = self.lookup(item)
            node.add(Node(item))
            self.balance(node)

    @property
    def unset(self):
        return self.root.data is None

    def balance(self, node: Node):
        for this in node.roots():
            left, right = map(self.height, this.children)
            diff = right - left
            p = diff > 0
            
            if abs(diff) > 1:
                next = this[p]                
                if self.height(next[p]) < self.height(next[not p]):
                    self.rotate(next, not p)
                
                self.rotate(this, p)
                break

    def rotate(self, node: Node, p: int): # p = 0: rotate right
        parent: Node = node.root
        next: Node = node[p]
        
        if parent is None:
            self.setroot(next)
        else:
            parent.replace(node, next)
            
        node.setchild(next[not p], p)
        next.setchild(node, not p)

    def lookup(self, item):
        if not self.unset:
            n = self.root
            while n is not None:
                yield n
                n = n.left if item < n.data else n.right
    
    def height(self, node, i=0):
        if node:
            return max(
                self.height(n, i+1)
                for n in node.children
            )
        return i

    def search(self, item) -> Node:
        for node in self.lookup(item):
            if node.data == item:
                return node

    def remove(self, item):
        node = self.search(item)
        if node is not None:
            self._remove(node)

    def _remove(self, node: Node):
        if all(node.children):
            most: Node = node.right
            while most.left: most = most.left
            node.data = most.data
            self._remove(most)
        else:
            child = next(filter(None, node)) if any(node) else None
            parent: Node = node.root
            if parent:
                parent.replace(node, child)
            else:
                self.setroot(child)
                
        self.balance(node)


avl_tree = AVL()
data = input('Enter the data of your friend: ')
line = '-' * 30
print(line)

for i in data.split(','):
    if i == 'P':
        for node, depth in avl_tree:
            if node or node is None:
                print(' ' * 4 * depth, 
                    '{1} ({0})'.format(*node.data)
                     if node else '*', sep=''
                )
        print(line)
        
    else:
        c, data = i.split()
        item = sum(map(ord, data)), data

        if c == 'I':
            avl_tree.add(item)
        elif c == 'D':
            avl_tree.remove(item)