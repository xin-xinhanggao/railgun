from BinNode import BinNode


def succ(node):
    # find the succ of the node
    if node.rc is not None:
        node = node.rc
        while True:
            if node.lc is not None:
                node = node.lc
            else:
                break
        return node
    y = node.p
    x = node
    while True:
        if y is not None and x == y.rc:
            x = y
            y = y.p
        else:
            break
    return y

