
"""Test Cases"""

from collections import deque
from dataStructures.linked_list_sum import sum_iterative
from dataStructures.linked_list_sum import sum_recursive


def test_sum_equal_size():
    assert sum_iterative(deque([3, 1, 5]), deque([5, 9, 2])) == deque(
        [8, 0, 8])  # 513 + 295 = 808


def test_sum_empty():
    assert sum_iterative(deque(), deque()) == deque()


def test_sum_one_empty():
    assert sum_iterative(deque([3, 1, 5]), deque()) == deque(
        [3, 1, 5])  # 513 + 0 = 513


def test_sum_different_size():
    assert sum_iterative(deque([3, 1, 5, 6]), deque(
        [5, 9, 2]))  # 6513 + 295 = 6808


def test_sum_recursive_equal_size():
    assert sum_recursive(deque([3, 1, 5]), deque([5, 9, 2])) == deque(
        [8, 0, 8])  # 513 + 295 = 808


def test_sum_recursive_empty():
    assert sum_recursive(deque(), deque()) == deque()


def test_sum_recursive_one_empty():
    assert sum_recursive(deque([3, 1, 5]), deque()) == deque(
        [3, 1, 5])  # 513 + 0 = 513


def test_sum_recursive_different_size():
    assert sum_recursive(deque([3, 1, 5, 6]), deque(
        [5, 9, 2]))  # 6513 + 295 = 6808
