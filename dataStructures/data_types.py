
"""Data Types Package"""


class LinkedListNode(object):
    """LinkedList Node"""

    def __init__(self, value):
        self._value = value
        self.next = None

    @property
    def value(self):
        return self._value


class LinkedList(object):
    """LinkedList (add-to-head version)"""

    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = LinkedListNode(value)
        node.next = self.head
        self.head = node

    def remove(self, value):
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
                return value

            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    return value

                current = current.next

        raise ValueError(str(value) + " not found")


class LinkedList2(object):
    """LinkedList (add-to-tail version)"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        node = LinkedListNode(value)
        if not self.head:
            self.head = node

        if not self.tail:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, value):
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
                if not self.head:
                    self.tail = None

                return value

            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    if not current.next:
                        self.tail = current

                    return value

                current = current.next

        raise ValueError(str(value) + " not found")


class Stack(object):
    """Stack"""

    def __init__(self):
        self._llist = LinkedList()

    def push(self, value):
        self._llist.add_to_head(value)

    def pop(self):
        return self._llist.remove(self._llist.head.value if self._llist.head else None)


class Queue(object):
    """Queue"""

    def __init__(self):
        self._llist = LinkedList2()

    def enqueue(self, value):
        self._llist.add_to_tail(value)

    def dequeue(self):
        return self._llist.remove(self._llist.head.value if self._llist.head else None)
