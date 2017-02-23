
"""Set of stacks Package"""


class SetOfStacks(object):
    """Set Of Stacks Class"""

    def __init__(self, capacity=3):
        self._stacks = []
        self._current = -1
        self._capacity = capacity

    def push(self, item):
        if self._current < 0 or len(self._stacks[self._current]) == self._capacity:
            self._add_stack()

        self._stacks[self._current].append(item)

    def pop(self):
        item = self._stacks[self._current].pop()
        if len(self._stacks[self._current]) == 0:
            self._remove_stack()

        return item

    def pop_at(self, index):
        if self._current < index:
            raise IndexError

        item = self._stacks[index].pop()
        self._shift_left(index)

        return item

    def _add_stack(self):
        self._stacks.append([])
        self._current += 1

    def _remove_stack(self):
        self._stacks.pop()
        self._current -= 1

    def _shift_left(self, index):
        if self._current == index:
            return

        for i in range(index, self._current):
            self._stacks[i].append(self._stacks[i + 1].pop())

        if len(self._stacks[self._current]) == 0:
            self._remove_stack()
