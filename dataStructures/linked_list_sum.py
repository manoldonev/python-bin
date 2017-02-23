
"""Linked List Sum Package"""

from collections import deque


def sum_iterative(num1, num2):
    """
    You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1's digit is at the head of
    the list. Write a function that adds the two numbers and returns the sum as a linked list.
    """
    # O(max{m,n}) time, O(max{m,n}) space
    carry = 0
    result = deque()
    while num1 or num2:
        digit_num1 = num1.popleft() if num1 else 0
        digit_num2 = num2.popleft() if num2 else 0

        temp = digit_num1 + digit_num2 + carry
        current = temp % 10
        carry = temp / 10
        result.append(current)

    return result


def sum_recursive(num1, num2, carry=0):
    """
    You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1's digit is at the head of
    the list. Write a function that adds the two numbers and returns the sum as a linked list.
    Recursive version
    """
    # O(max{m,n}) time, O(max{m,n}) space
    if not num1 and not num2:
        return deque()

    digit_num1 = num1.popleft() if num1 else 0
    digit_num2 = num2.popleft() if num2 else 0
    temp = digit_num1 + digit_num2 + carry

    result = sum_recursive(num1, num2, temp / 10)
    result.appendleft(temp % 10)

    return result
