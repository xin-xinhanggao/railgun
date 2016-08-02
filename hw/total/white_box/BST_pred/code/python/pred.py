from BinNode import BinNode


def pred(node):
    # find the pred of the node
    if node.lc is not None:
        node = node.lc
        while True:
            if node.rc is not None:
                node = node.rc
            else:
                break
        return node
    y = node.p
    x = node
    while True:
        if y is not None and x == y.lc:
            x = y
            y = y.p
        else:
            break
    return y

