
"""Linked Lists from BST"""

from dataStructures.data_types import LinkedList
from dataStructures.data_types_bst import BinaryTreeNode


def linked_lists_from_bst(root):
    level = 0
    llist_root = LinkedList()
    llist_root.add_to_head(root)
    result = [llist_root]

    while True:
        llist = LinkedList()
        current = result[level].head
        while current:
            if current.value.left:
                llist.add_to_head(current.value.left)

            if current.value.right:
                llist.add_to_head(current.value.right)

            current = current.next

        if llist.head:
            result.append(llist)
            level += 1
        else:
            break

    return result
