class BinNode:
    def __init__(self, parent=None, value = 0):
        # init the binary node
        self.p = parent
        self.lc = None
        self.rc = None
        self.v = 0
    
    def set_v(self, value):
        # set the value of the node
        self.v = value
    
    def set_p(self, node):
        # set the parent of the node
        self.p = node
    
    def set_lc(self, node):
        # set the left child of the node
        self.lc = node
    
    def set_rc(self, node):
        # set the right child of the node
        self.rc = node
    
    def is_lc(self):
        # check whether the node is left child of parent node
        if self.p is None:
            return False
        
        return self.p.lc == self
    
    def is_rc(self):
        # check whether the node is right child of parent node
        if self.p is None:
            return False
        
        return self.p.rc == self
    
    def has_lc(self):
        # check whether the node has left child
        return self.lc is not None
    
    def has_rc(self):
        # check whether the node has right child
        return self.rc is not None
    
    def tree_min(self):
        # find the minimum node of the subtree
        x = self
        while x.lc is not None:
            x = x.lc
        return x
            
    def succ(self):
        # find the succ of the node
        if self.rc is not None:
            return self.rc.tree_min()
        y = self.p
        while y is not None and x == y.rc:
            x = y
            y = y.p
        return y

