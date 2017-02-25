
"""Data Types Tree Package"""


class TreeNode(object):
    """Tree Node"""

    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, key):
        if self.key == key:
            return self

        if self.key > key:
            return self.left.find(key) if self.left else None
        else:
            return self.right.find(key) if self.right else None

    def insert(self, key):
        if self.key >= key:
            if not self.left:
                self.left = TreeNode(key, self)
                return self.left

            return self.left.insert(key)
        elif not self.right:
            self.right = TreeNode(key, self)
            return self.right
        else:
            return self.right.insert(key)

    def traverse_in_order(self):
        if self.left:
            for node in self.left.traverse_in_order():
                yield node

        yield self

        if self.right:
            for node in self.right.traverse_in_order():
                yield node

    def minimum(self):
        if not self.left:
            return self

        return self.left.minimum()

    def maximum(self):
        if not self.right:
            return self

        return self.right.maximum()

    def predecessor(self, key):
        node = self.find(key)
        if not node:
            return None

        if node.left:
            return node.left.maximum()

        predecessor = None
        current = node.parent
        while current:
            if current.key < key:
                predecessor = current
                break

            current = current.parent

        return predecessor

    def successor(self, key):
        node = self.find(key)
        if not node:
            return None

        if node.right:
            return node.right.minimum()

        successor = None
        current = node.parent
        while current:
            if current.key > key:
                successor = current
                break

            current = current.parent

        return successor


class BinarySearchTree(object):
    """Binary Search Tree"""

    def __init__(self):
        self.root = None

    def __iter__(self):
        if not self.root:
            return

        for node in self.root.traverse_in_order():
            yield node

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
            return self.root

        return self.root.insert(key)

    def find_node(self, key):
        if not self.root:
            return None

        return self.root.find(key)

    def minimum(self):
        if not self.root:
            return None

        return self.root.minimum()

    def maximum(self):
        if not self.root:
            return None

        return self.root.maximum()

    def predecessor(self, key):
        if not self.root:
            return None

        return self.root.predecessor(key)

    def successor(self, key):
        if not self.root:
            return None

        return self.root.successor(key)
