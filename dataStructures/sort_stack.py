
"""Sort Stack Package"""


def sort_stack(stack):
    """
    Write a program to sort a stack in ascending order. You should not make any assumptions about
    how the stack is implemented. The following are the only functions that should be used to write
    this program: push | pop | peek | isEmpty
    """
    # O(n^2) time, O(n) space
    stack_sorted = []
    current = None
    while stack:
        current = stack.pop()
        while stack_sorted and stack_sorted[len(stack_sorted) - 1] > current:
            stack.append(stack_sorted.pop())

        stack_sorted.append(current)

    return stack_sorted
