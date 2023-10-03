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

    def spread(self, node: Node, prev=None):
        next: Node
        for next in [*node, node.root]:
            if next and next is not prev:
                yield next

    def burn(self, item):
        f = self.search(item)
        
        if f is None:
            yield f'There is no {item} in the tree.',
            
        else:
            node = {f: None}
            while node:
                yield node
                node = {
                    new: now 
                    for now, prev in node.items()
                    for new in self.spread(now, prev)
                }
        
    def setroot(self, node=None):
        node = node or Node(None)
        self.root = node
        node.root = None

    @property
    def unset(self):
        return self.root.data is None
             
    def add(self, item):
        if self.unset:
            self.root.data = item
        else:
            *_, node = self.lookup(item)
            node.add(Node(item))
            self.balance(node)

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

avl_tree = AVL()
data, s = input('Enter node and burn node : ').split('/')

for n in map(int, data.split()):
    avl_tree.add(n)

for nodes in avl_tree.burn(int(s)):
    print(*nodes)