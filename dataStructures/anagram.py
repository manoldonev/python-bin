
"""Anagram Strings Package"""

from collections import Counter


def anagram_counter(s1, s2):
    """Write a method to decide if two strings are anagrams or not."""
    # O(n) time, O(n) space
    return Counter(s1) == Counter(s2)


def anagram_sorted(s1, s2):
    """Write a method to decide if two strings are anagrams or not."""
    # O(nlogn) time, O(n) space
    return sorted(s1) == sorted(s2)
