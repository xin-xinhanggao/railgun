class BinNode:
    def __init__(self, parent=None):
        # init the binary node
        self.p = parent
        self.lc = None
        self.rc = None
    
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
    
    def succ(self):
        # find the succ of the node
        if self.rc is None and self.p is None:
            return None
        if self.rc is None:
            return self.p
        current = self.rc
        while current is not None:
            if current.lc is None:
                return current
            else:
                current = current.lc
