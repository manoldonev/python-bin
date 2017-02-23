
"""Test Cases"""

from dataStructures.set_of_stacks import SetOfStacks
from nose.tools import assert_raises


def test_set_of_stacks():
    stacks = SetOfStacks()
    stacks.push(1)
    assert stacks._current == 0
    assert len(stacks._stacks) == 1

    stacks.push(2)
    assert stacks._current == 0
    assert len(stacks._stacks) == 1

    assert stacks.pop() == 2
    assert stacks._current == 0
    assert len(stacks._stacks) == 1

    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    assert stacks._current == 1
    assert len(stacks._stacks) == 2

    assert stacks.pop() == 5
    assert stacks._current == 1
    assert len(stacks._stacks) == 2

    assert stacks.pop() == 4
    assert stacks._current == 0
    assert len(stacks._stacks) == 1

    assert stacks.pop() == 3
    stacks.push(3)
    assert stacks._current == 0
    assert len(stacks._stacks) == 1

    stacks.push(4)
    stacks.push(5)
    stacks.push(6)
    stacks.push(7)

    assert_raises(IndexError, stacks.pop_at, 4)

    assert stacks.pop_at(1) == 6
    assert stacks._current == 1
    assert len(stacks._stacks) == 2

    assert stacks.pop() == 7
