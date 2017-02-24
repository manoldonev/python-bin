
"""Test Cases"""

from dataStructures.myqueue import MyQueue


def test_myqueue():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    assert queue._stacks[0] == [3, 2, 1]
    assert queue._stacks[1] == []
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
