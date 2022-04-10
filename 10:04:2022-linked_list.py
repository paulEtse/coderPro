#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def value_from_node(self):
        current_node = self
        i = 0
        n = current_node.val * 10 ** i
        while current_node.next is not None:
            i += 1
            n = n + current_node.next.val * 10 ** i
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


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
assert l1.value_from_node() == 342

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
assert l2.value_from_node() == 465

result = Solution().addTwoNumbers(l1, l2)
print(result)
# 7 0 8
