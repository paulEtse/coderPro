import unittest

from src._04_2022._21_04_2022.invert_binary_tree import invert
from utils.binarySearchTree.binary_search_tree import Node


class TestSolution(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = Node("a")
        root.left = Node("b")
        root.right = Node("c")
        root.left.left = Node("d")
        root.left.right = Node("e")
        root.right.left = Node("f")
        self.assertTrue(invert(root).preorder(), "acfbed")
