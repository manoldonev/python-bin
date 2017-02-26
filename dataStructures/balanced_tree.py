
"""Balanced Tree Package"""

from dataStructures.data_types_bst import BinaryTreeNode


def is_balanced(root):
    return max_depth(root) - min_depth(root) <= 1


def min_depth(node):
    if node == None:
        return 0

    return 1 + min(min_depth(node.left), min_depth(node.right))


def max_depth(node):
    if node == None:
        return 0

    return 1 + max(max_depth(node.left), max_depth(node.right))
