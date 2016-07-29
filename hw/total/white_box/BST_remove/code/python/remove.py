from BinNode import BinNode


def remove(BinNode x):
    if not x.has_lc:
        # replace node x with its right child
        return "rChild"
    elif not x.has_rc:
        # replace node x with its left child
        return "lChild"
    else:
        # node x has two childs
        if x.p == None:
            return "x->rChild"
        else:
            w = x.succ()
            u = w.p
            if u == x:
                return "u->rChild"
            else:
                return "u->lChild"
