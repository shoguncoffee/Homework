class Node:
    attr = 'left', 'right'
    
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
            root: Node
            yield root
            root = root.root

    def setchild(self, node, p: int):
        setattr(self, Node.attr[p], node)
        
        if node is not None:
            node.root = self
            
    def add(self, node):
        condition = node.data < self.data
        
        if self.left is None and condition:
            self.left = node
            
        elif self.right is None and not condition: 
            self.right = node

    def __getitem__(self, key):
        return self.children[key]

    def __repr__(self):
        return str(self.data)

    @property
    def is_leaf(self):
        return self.left is self.right is None


class AVL:
    def __init__(self):
        self.setroot(Node(None))

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

    def setroot(self, node: Node):
        self.root = node
        node.root = None
             
    def add(self, item):
        if self.root.data is None:
            self.root.data = item
        else:
            node = self.search(item)
            node.add(Node(item, node))
            self.balance(node)

    def balance(self, node: Node):
        for this in node.roots():
            left, right = map(self.height, this.children)
            diff = right - left
            p = diff > 0
            
            if abs(diff) > 1:
                print('Not Balance, Rebalance!')
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
            i = parent.children.index(node)
            parent.setchild(next, i)
            
        node.setchild(next[not p], p)
        next.setchild(node, not p)

    def lookup(self, item):
        n = self.root
        while n:
            next = n.left if item < n.data else n.right
            yield n, next
            n = next
               
    def size(self, node: Node):
        if node:
            tree = *self.iter(node),
            return len(tree)
        return 0
    
    def depth(self, node: Node):
        return len(list(node.roots()))

    def height(self, node, i=0):
        if node:
            return max(
                self.height(n, i+1)
                for n in node.children
            )
        return i
  
avl = AVL() 
for data in map(int, input('Enter Input : ').split()):
    print('insert :', data)
    node = avl.add(data)
    
    for node in avl:
        print(5 * ' ' * avl.depth(node), node)
        
    print('='*15)