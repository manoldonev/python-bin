
"""Test Cases"""

from dataStructures.hanoi_towers import hanoi


def test_hanoi_3_discs():
    assert repr(hanoi(3)) == "[[], [], [3, 2, 1]]"


def test_hanoi_7_discs():
    assert repr(hanoi(7)) == "[[], [], [7, 6, 5, 4, 3, 2, 1]]"
