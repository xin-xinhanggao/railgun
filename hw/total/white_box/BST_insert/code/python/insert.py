from BinNode import BinNode
from Tree import Tree


def remove(T,z):
    # insert BinNode z into Tree T
    y = None
    x = T.root
    while x != None:
        y = x
        if x.v < z.v:
            x = x.lc
        elif x.v == z.v:
            return False
        else:
            x = x.rc
    z.set_p(y)
    if y == None:
        T.root = z
        return True
    else:
        if z.v > y.v:
            y.set_rc(z)
        else:
            y.set_lc(z)
        return True

