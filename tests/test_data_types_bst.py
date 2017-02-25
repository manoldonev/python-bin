
"""Test Cases"""

from dataStructures.data_types_bst import BinarySearchTree


def test_bst_insert():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)

    assert tree.root.key == 5
    assert tree.root.left.key == 1
    assert tree.root.left.left is None
    assert tree.root.left.right.key is 3
    assert tree.root.left.right.left.key == 2
    assert tree.root.left.right.right.key == 4
    assert tree.root.left.right.left.left is None
    assert tree.root.left.right.left.right is None
    assert tree.root.left.right.right.left is None
    assert tree.root.left.right.right.right is None
    assert tree.root.right.key == 6
    assert tree.root.right.left is None
    assert tree.root.right.right is None


def test_bst_insert_identical_keys():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(5)
    tree.insert(1)
    tree.insert(6)
    tree.insert(6)

    assert tree.root.key == 5
    assert tree.root.left.key == 1
    assert tree.root.left.left.key == 1
    assert tree.root.left.right.key == 5
    assert tree.root.right.key == 6
    assert tree.root.right.left.key == 6


def test_bst_in_order_traversal():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)

    assert [node.key for node in tree] == [1, 2, 3, 4, 5, 6]


def test_bst_in_order_traversal_identical_keys():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(5)
    tree.insert(1)
    tree.insert(6)
    tree.insert(6)

    assert [node.key for node in tree] == [1, 1, 5, 5, 6, 6]


def test_bst_in_order_traversal_empty():
    tree = BinarySearchTree()

    assert [node.key for node in tree] == []


def test_bst_minimum():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)

    assert tree.minimum().key == 1
    assert tree.minimum().left is None


def test_bst_minimum_identical_keys():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(5)
    tree.insert(1)
    tree.insert(6)
    tree.insert(6)

    assert tree.minimum().key == 1
    assert tree.minimum().left is None


def test_bst_maximum():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)

    assert tree.maximum().key == 6
    assert tree.maximum().right is None


def test_bst_maximum_identical_keys():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(5)
    tree.insert(1)
    tree.insert(6)
    tree.insert(6)

    assert tree.maximum().key == 6
    assert tree.maximum().right is None


def test_bst_predecessor():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)

    assert tree.predecessor(6).key == 5
    assert tree.predecessor(7) is None
    assert tree.predecessor(1) is None
    assert tree.predecessor(4).key == 3


def test_bst_successor():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)

    assert tree.successor(6) is None
    assert tree.successor(4).key == 5
    assert tree.successor(2).key == 3


def test_bst_remove_no_children():
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)

    two_node = tree.find(2)
    assert two_node is not None
    assert two_node.parent.key == 1

    tree.remove(2)
    two_node = tree.find(2)
    assert two_node is None
    assert tree.root.left.right is None


def test_bst_remove_one_child():
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)

    five_node = tree.find(5)
    assert five_node is not None
    assert five_node.parent.key == 3

    tree.remove(5)
    five_node = tree.find(5)
    assert five_node is None
    assert tree.root.right.key == 4
    assert tree.root.right.right is None
    assert tree.root.right.left is None


def test_bst_remove_two_children():
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)

    three_node = tree.find(3)
    assert three_node is not None
    assert three_node == tree.root

    tree.remove(3)
    three_node = tree.find(3)
    assert three_node is None
    assert tree.root.key == 2
    assert tree.root.left.right is None


def test_bst_remove_single_node():
    tree = BinarySearchTree()
    tree.insert(3)

    tree.remove(3)
    assert tree.root is None


def test_bst_remove_root():
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(1)

    tree.remove(3)
    assert tree.root.key == 1
