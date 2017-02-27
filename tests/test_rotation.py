
"""Test Cases"""

from dataStructures.string_rotation import rotation


def test_rotation():
    assert rotation("waterbottle", "erbottlewat")


def test_not_rotation():
    assert rotation("waterbottle", "bottlebottle") is False


def test_not_rotation2():
    assert rotation("waterbottle", "bottle") is False
