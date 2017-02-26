
"""Test Cases"""

from dataStructures.balanced_tree import is_balanced
from dataStructures.data_types_bst import BinaryTreeNode


def test_chain_not_balanced():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(3)

    assert not is_balanced(root)


def test_root_balanced():
    root = BinaryTreeNode(1)

    assert is_balanced(root)


def test_complete_tree_balanced():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    assert is_balanced(root)


def test_balanced_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(5)
    root.right.right = BinaryTreeNode(7)

    assert is_balanced(root)
