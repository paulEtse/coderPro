#!/usr/bin/python3


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def value_from_node(self):
        current_node = self
        i = 0
        n = current_node.val * 10**i
        while current_node.next is not None:
            i += 1
            n = n + current_node.next.val * 10**i
            current_node = current_node.next
        return n

    def node_from_value(value):
        root = ListNode(int(value % 10))
        node = root
        value //= 10
        while value != 0:
            node.next = ListNode(value % 10)
            value //= 10
            node = node.next
        return root

    def __str__(self):
        current = self
        res = ""
        while current.next is not None:
            res += str(current.val)
            current = current.next
        res += str(current.val)
        return res


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        return ListNode.node_from_value(l1.value_from_node() + l2.value_from_node())
