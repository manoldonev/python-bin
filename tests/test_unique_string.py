
"""Test Cases"""

from dataStructures.unique_string import unique
from dataStructures.unique_string import unique2
from dataStructures.unique_string import unique3
from dataStructures.unique_string import unique4

def test_unique():
    assert unique("abcdefg") == True


def test_unique_empty():
    assert unique("") == True


def test_not_unique_1():
    assert unique("aabcdefg") == False


def test_not_unique_2():
    assert unique("abcdefgg") == False


def test_not_unique_3():
    assert unique("aaa") == False


def test_unique2():
    assert unique2("abcdefg") == True


def test_unique2_empty():
    assert unique2("") == True


def test_not_unique2_1():
    assert unique2("aabcdefg") == False


def test_not_unique2_2():
    assert unique2("abcdefgg") == False


def test_not_unique2_3():
    assert unique2("aaa") == False


def test_unique3():
    assert unique3("abcdefg") == True


def test_unique3_empty():
    assert unique3("") == True


def test_not_unique3_1():
    assert unique3("aabcdefg") == False


def test_not_unique3_2():
    assert unique3("abcdefgg") == False


def test_not_unique3_3():
    assert unique3("aaa") == False


def test_unique4():
    assert unique4("abcdefg") == True


def test_unique4_empty():
    assert unique4("") == True


def test_not_unique4_1():
    assert unique4("aabcdefg") == False


def test_not_unique4_2():
    assert unique4("abcdefgg") == False


def test_not_unique4_3():
    assert unique4("aaa") == False
