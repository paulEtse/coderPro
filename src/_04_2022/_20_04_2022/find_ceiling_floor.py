def findCeilingFloor(root_node, k, floor=None, ceil=None):
    while root_node is not None:
        if k == root_node.value:
            return (k, k)
        elif k > root_node.value:
            floor = root_node.value
            root_node = root_node.right
        else:
            ceil = root_node.value
            root_node = root_node.left
    return (floor, ceil)
