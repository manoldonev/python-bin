
"""Test Cases"""

from dataStructures.anagram import anagram_prime
from dataStructures.anagram import anagram_sorted
from dataStructures.anagram import anagram_counter


def test_anagram_prime():
    assert anagram_prime("abcde", "bcdae")


def test_anagram_prime2():
    assert anagram_prime("", "")


def test_not_anagram_prime3():
    assert anagram_prime("abcde", "bcdaf") is False


def test_not_anagram_prime4():
    assert anagram_prime("abcde", "") is False


def test_anagram_sorted():
    assert anagram_sorted("abcde", "bcdae")


def test_anagram_sorted2():
    assert anagram_sorted("", "")


def test_not_anagram_sorted3():
    assert anagram_sorted("abcde", "bcdaf") is False


def test_not_anagram_sorted4():
    assert anagram_sorted("abcde", "") is False


def test_anagram_counter():
    assert anagram_counter("abcde", "bcdae")


def test_anagram_counter2():
    assert anagram_counter("", "")


def test_not_anagram_counter3():
    assert anagram_counter("abcde", "bcdaf") is False


def test_not_anagram_counter4():
    assert anagram_counter("abcde", "") is False
