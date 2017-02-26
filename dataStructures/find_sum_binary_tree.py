
"""Find Sum Package"""


def find_sum(root, desired_sum, level=0, buffer_list=None, result=[]):
    """
    You are given a binary tree in which each node contains a value
    Design an algorithm to print all paths which sum up to that value
    Note that it can be any path in the tree - it does not have to start at the root
    """
    if not buffer_list:
        buffer_list = []

    if not root:
        return result

    buffer_list.append(root.key)
    temp = desired_sum

    for i in range(level, -1, -1):
        temp -= buffer_list[i]

        if temp == 0:
            result.append(buffer_list[i:level + 1])

    find_sum(root.left, desired_sum, level + 1, buffer_list[:], result)
    find_sum(root.right, desired_sum, level + 1, buffer_list[:], result)

    return result
