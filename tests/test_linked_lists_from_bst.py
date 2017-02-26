
"""Test Cases"""

from dataStructures.data_types_bst import BinaryTreeNode
from dataStructures.linked_lists_from_bst import linked_lists_from_bst


def test_linked_lists_from_bst():
    root = BinaryTreeNode(7)
    root.insert(6)
    root.insert(5)
    root.insert(4)
    root.insert(2)
    root.insert(1)
    root.insert(3)
    root.insert(8)
    root.insert(9)

    res = []
    for llist in linked_lists_from_bst(root):
        current = llist.head
        l = []
        while current:
            l.append(current.value.key)
            current = current.next

        res.append(l)

    assert res == [[7], [8, 6], [5, 9], [4], [2], [3, 1]]
