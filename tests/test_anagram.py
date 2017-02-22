
"""Test Cases"""

from dataStructures.anagram import anagram_sorted
from dataStructures.anagram import anagram_counter


def test_anagram_sorted():
    assert anagram_sorted("abcde", "bcdae") == True


def test_anagram_sorted2():
    assert anagram_sorted("", "") == True


def test_not_anagram_sorted3():
    assert anagram_sorted("abcde", "bcdaf") == False


def test_not_anagram_sorted4():
    assert anagram_sorted("abcde", "") == False


def test_anagram_counter():
    assert anagram_counter("abcde", "bcdae") == True


def test_anagram_counter2():
    assert anagram_counter("", "") == True


def test_not_anagram_counter3():
    assert anagram_counter("abcde", "bcdaf") == False


def test_not_anagram_counter4():
    assert anagram_counter("abcde", "") == False
