from BinNode import BinNode


def splay(v):  # BinNode v
    # simulate the splay process of splay tree
    if v is None:
        return "None"

    p = v.p  # the father of v

    if p is not None:
        g = p.p  # the grandfather of v
    else:
        g = None

    if g is not None:
        gg = g.p  # the great-grandfather of v
    else:
        gg = None

    if gg is not None:
        return "root"

    if v.is_lc() and p is not None:  # the main process of splay
        if p.is_lc():
            return "zig-zig"
        else:
            return "zig-zag"
    elif p is not None and p.is_rc():
        return "zag-zag"
    else:
        return "zag-zig"
