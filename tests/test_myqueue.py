
"""Test Cases"""

from dataStructures.myqueue import MyQueue


def test_myqueue():
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue._stacks[0] == [3, 2, 1]
    assert queue._stacks[1] == []
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
