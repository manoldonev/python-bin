
"""Test Cases"""

from dataStructures.deduplicate_anagrams import deduplicate_anagrams


def test_deduplicate_anagrams():

    assert deduplicate_anagrams([
        "arc",
        "abac",
        "aabc",
        "cbaa",
        "car",
        "word"
    ]) == ['abac', 'word', 'car']
