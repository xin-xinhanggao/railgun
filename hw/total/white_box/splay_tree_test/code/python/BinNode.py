class BinNode:
    def __init__(self, parent=None):
        # init the binary node
        self.p = parent
        self.lc = None
        self.rc = None

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
