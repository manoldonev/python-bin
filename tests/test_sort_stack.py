
"""Test Cases"""

from dataStructures.sort_stack import sort_stack


def test_sort_stack():
    assert sort_stack([4, 1, 2, 5, 3]) == [1, 2, 3, 4, 5]


def test_sort_stack_empty():
    assert sort_stack([]) == []


def test_sort_stack_already_sorted():
    assert sort_stack([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_sort_stack_reversed():
    assert sort_stack([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
