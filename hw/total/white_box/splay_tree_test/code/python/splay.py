from BinNode import BinNode

def splay(v): #BinNode v
#simulate the splay process of splay tree
    if v == None:
        return "None"

    p = v.p #the father of v

    if p != None:
        g = p.p #the grandfather of v
    else:
        g = None

    if g != None:
        gg = g.p #the great-grandfather of v
    else:
        gg = None

    if gg == None:
        return "root"

    if v.is_lc():#the main process of splay
        if p != None:
            if p.is_lc():
                return "zig-zig"
            else:
                return "zig-zag"
        else:
            return "zig-zag"
    elif p != None and p.is_rc():
        return "zag-zag"
    else:
        return "zag-zig"

