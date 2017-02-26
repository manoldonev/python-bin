
"""Data Types Tree Package"""


class BinaryTreeNode(object):
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
                self.left = BinaryTreeNode(key, self)
                return self.left

            return self.left.insert(key)
        elif not self.right:
            self.right = BinaryTreeNode(key, self)
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

    def remove(self, root):
        if self.left and self.right:
            # we know it exists and it is max of left subtree (no left child)
            predecessor = self.predecessor()
            # swap node-to-remove with its predecessor
            self.key, predecessor.key = predecessor.key, self.key
            # remove predecessor (no left child for sure => simpler case)
            predecessor.remove(root)
        elif self.left:
            if self == root:
                root = self.left
            elif self.parent.left == self:
                self.parent.left = self.left
            else:
                self.parent.right = self.left
        elif self.right:
            if self == root:
                root = self.right
            elif self.parent.left == self:
                self.parent.left = self.right
            else:
                self.parent.right = self.right
        else:
            if self == root:
                root = None
            elif self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None

        return root

    def predecessor(self):
        if self.left:
            return self.left.maximum()

        predecessor = None
        current = self.parent
        while current:
            if current.key < self.key:
                predecessor = current
                break

            current = current.parent

        return predecessor

    def successor(self):
        if self.right:
            return self.right.minimum()

        successor = None
        current = self.parent
        while current:
            if current.key > self.key:
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
            self.root = BinaryTreeNode(key)
            return self.root

        return self.root.insert(key)

    def remove(self, key):
        node = self.find(key)
        if not node:
            return

        self.root = node.remove(self.root)

        return self.root

    def find(self, key):
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
        node = self.find(key)
        if not node:
            return None

        return node.predecessor()

    def successor(self, key):
        node = self.find(key)
        if not node:
            return None

        return node.successor()
