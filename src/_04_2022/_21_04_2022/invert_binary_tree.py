from utils.binarySearchTree.binary_search_tree import Node


def invert(node):
    if node is None:
        return node
    res = Node(node.value)
    node.left = invert(node.right)
    node.right = invert(node.left)
    return res
