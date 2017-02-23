
"""Hanoi Towers Package"""


class Tower(object):

    def __init__(self, index):
        self.discs = []
        self.index = index

    def add_disc(self, i):
        if self.discs and self.discs[len(self.discs) - 1] <= i:
            raise ValueError

        self.discs.append(i)

    def move_discs(self, n, destination, buffer):
        if n > 0:
            self.move_discs(n - 1, buffer, destination)
            destination.add_disc(self.discs.pop())
            buffer.move_discs(n - 1, destination, self)

    def __repr__(self):
        return repr(self.discs)


def hanoi(n):
    """
    The classic problem of the Towers of Hanoi
    """
    # T(n) = 2^n - 1
    towers = [Tower(i) for i in range(0, 3)]
    for j in range(n, 0, -1):
        towers[0].add_disc(j)

    towers[0].move_discs(n, towers[2], towers[1])

    return towers
