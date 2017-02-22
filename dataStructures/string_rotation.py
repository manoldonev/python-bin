
"""String Rotation"""


def rotation(s1, s2):
    """Given two strings, s1 and s2, write code to check if s2 is a rotation
    of s1 using only one call to isSubstring."""
    if len(s1) != len(s2):
        return False

    s1 *= 2
    return s1.find(s2) != -1
