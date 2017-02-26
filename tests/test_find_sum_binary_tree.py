
"""Test Cases"""

from dataStructures.data_types_bst import BinaryTreeNode
from dataStructures.find_sum_binary_tree import find_sum


def test_find_sum():
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(-4)
    root.left.right.left = BinaryTreeNode(3)
    root.left.right.left.left = BinaryTreeNode(1)
    root.left.right.left.left.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(-1)
    root.right.right = BinaryTreeNode(-2)
    root.right.right.left = BinaryTreeNode(2)
    root.right.right.right = BinaryTreeNode(3)
    root.right.right.right.left = BinaryTreeNode(2)
    root.right.right.right.left.left = BinaryTreeNode(1)

    assert find_sum(root, 5) == [
        [2, 3], [2, 3, -4, 3, 1], [3, -4, 3, 1, 2], [3, 2], [2, -1, -2, 3, 2, 1]]
