
"""Anagram Strings Package"""

from collections import Counter


def anagram_prime(s1, s2):
    """Write a method to decide if two strings are anagrams or not."""

    # O(n) time, O(1) space
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    product1 = 1
    for char1 in s1:
        product1 *= primes[ord(char1) - 97]

    product2 = 1
    for char2 in s2:
        product2 *= primes[ord(char2) - 97]

    return product1 == product2


def anagram_counter(s1, s2):
    """Write a method to decide if two strings are anagrams or not."""

    # O(n) time, O(n) space
    return Counter(s1) == Counter(s2)


def anagram_sorted(s1, s2):
    """Write a method to decide if two strings are anagrams or not."""

    # O(nlogn) time, O(n) space
    return sorted(s1) == sorted(s2)
