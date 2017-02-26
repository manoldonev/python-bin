
"""BST from Sorted Array Package"""

from data_types_bst import BinaryTreeNode


def bst_from_sorted_array(l):
    """BST from sorted array"""

    n = len(l)
    if n == 0:
        return

    i = len(l) / 2
    node = BinaryTreeNode(l[i])
    node.left = bst_from_sorted_array(l[:i])
    node.right = bst_from_sorted_array(l[i + 1:])

    return node
