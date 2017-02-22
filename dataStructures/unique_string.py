
def unique(s):
    """Implement an algorithm to determine if a string has all unique characters."""
    # O(n) time, O(n) space
    explored = set()
    for char in s:
        if char in explored:
            return False

        explored.add(char)

    return True


def unique2(s):
    """Implement an algorithm to determine if a string has all unique characters."""
    # O(n) time, O(n) space
    return len(set(s)) == len(s)


def unique3(s):
    """Implement an algorithm to determine if a string has all unique characters. What if you
    can not use additional data structures?"""
    # O(nlogn) time, no space (quicksort)
    previous = None
    for char in sorted(s):
        if char == previous:
            return False

        previous = char

    return True


def unique4(s):
    """Implement an algorithm to determine if a string has all unique characters. What if you
    can not use additional data structures?"""
    # Time complexity is O(n^2), no space
    n = len(s)
    for i in range(0, n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return False

    return True
