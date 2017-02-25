
"""MyQueue Package"""


class MyQueue(object):
    """Implement a MyQueue class which implements a queue using two stacks"""

    def __init__(self):
        self._stacks = [[], []]

    def enqueue(self, item):
        while self._stacks[0]:
            self._stacks[1].append(self._stacks[0].pop())

        self._stacks[0].append(item)

        while self._stacks[1]:
            self._stacks[0].append(self._stacks[1].pop())

    def dequeue(self):
        return self._stacks[0].pop()
