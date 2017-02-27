
"""Deduplicate Anagrams Package"""

from collections import Counter


def deduplicate_anagrams(words):
    """Deduplicate anagrams in a list of n words with at most k characters"""
    # O(nk) time complexity

    words_hash = {}
    # O(nk) n times at most k inserts in a hashtable + additional constant operations
    for word in words:
        words_hash[word] = tuple(
            value * key for key, value in Counter(word).iteritems())

    # remove duplicates per anagram group
    # O(n) - n inserts in set (hashtable)
    anagram_groups = {tuple_repr for tuple_repr in words_hash.itervalues()}

    result = []
    # O(n) - n times constant operations
    for word, tuple_repr in words_hash.iteritems():
        if tuple_repr in anagram_groups:
            result.append(word)
            anagram_groups.remove(tuple_repr)

    return result
