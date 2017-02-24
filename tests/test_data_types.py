
"""Test Cases"""

from nose.tools import assert_raises
from dataStructures.data_types import LinkedList
from dataStructures.data_types import LinkedList2
from dataStructures.data_types import Stack
from dataStructures.data_types import Queue


def test_llist_remove_from_empty():
    llist = LinkedList()

    assert_raises(ValueError, llist.remove, 4)


def test_llist_remove_missing():
    llist = LinkedList()
    llist.add_to_head(1)
    llist.add_to_head(2)
    llist.add_to_head(3)

    assert_raises(ValueError, llist.remove, 4)


def test_llist_add_to_front():
    llist = LinkedList()
    assert llist.head is None

    llist.add_to_head(1)
    assert llist.head.value == 1

    llist.add_to_head(2)
    assert llist.head.value == 2

    llist.add_to_head(3)
    assert llist.head.value == 3

    llist.remove(3)
    assert llist.head.value == 2

    llist.remove(1)
    assert llist.head.value == 2

    llist.remove(2)
    assert llist.head is None


def test_llist2_remove_from_empty():
    llist = LinkedList2()

    assert_raises(ValueError, llist.remove, 4)


def test_llist2_remove_missing():
    llist = LinkedList2()
    llist.add_to_tail(1)
    llist.add_to_tail(2)
    llist.add_to_tail(3)

    assert_raises(ValueError, llist.remove, 4)


def test_llist2():
    llist = LinkedList2()
    assert llist.head is None
    assert llist.tail is None

    llist.add_to_tail(1)
    assert llist.head.value == 1
    assert llist.tail.value == 1

    llist.add_to_tail(2)
    assert llist.head.value == 1
    assert llist.tail.value == 2

    llist.add_to_tail(3)
    assert llist.head.value == 1
    assert llist.tail.value == 3

    llist.add_to_tail(4)
    assert llist.head.value == 1
    assert llist.tail.value == 4

    llist.remove(4)
    assert llist.head.value == 1
    assert llist.tail.value == 3

    llist.remove(2)
    assert llist.head.value == 1
    assert llist.tail.value == 3

    llist.remove(1)
    assert llist.head.value == 3
    assert llist.tail.value == 3

    llist.remove(3)
    assert llist.head is None
    assert llist.tail is None


def test_stack_pop_empty():
    stack = Stack()

    assert_raises(ValueError, stack.pop)


def test_stack():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_queue_dequeue_empty():
    queue = Queue()

    assert_raises(ValueError, queue.dequeue)


def test_queue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
