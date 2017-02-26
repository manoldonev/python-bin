
"""Test Cases"""

from dataStructures.data_types_bst import BinarySearchTree
from dataStructures.bst_from_sorted_array import bst_from_sorted_array


def test_bst_from_sorted_array():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = bst_from_sorted_array(l)
    tree = BinarySearchTree(root)

    assert [node.key for node in tree] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
