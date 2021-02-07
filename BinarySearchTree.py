from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        BinaryTree.__init__(self)
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
    
        
    def find_last(self, x : object) -> BinaryTree.Node:
        # todo
        w = self.r
        prev = None
        while w != self.nil:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        # todo
        if u == self.nil:
            raise Exception()
        if p == self.nil:
            self.r = u #inserting into an empty tree
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else: #u.x already exists in the tree
                return False
            u.parent = p
        self.n += 1

    def find_eq(self, x : object) -> object:
        # todo
        w = self.r
        while w != self.nil:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return None
    
    def find(self, x: object) -> object:
        # todo
        w = self.r
        z = self.nil
        while w != self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.v
        if z == self.nil:
            return None

        return z.v
        
    def add(self, key : object, value : object) -> bool:
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)
    
    def splice(self, u: BinaryTree.Node):
        # todo
        if u.left != self.nil:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != self.nil:
            s.parent = p
        self.n -= 1

    def remove_node(self, u : BinaryTree.Node):
        # todo
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            w = u.right
            while w.left != self.nil:
                w = w.left
            u.x = w.x
            self.splice(w)

    def remove(self, x : object) -> bool:
        # todo
        w = self.find_eq(x)
        if w is None:
            return False
        self.remove_node(w)
        return True
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)


            
