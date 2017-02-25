
"""Data Types Graph"""

from collections import deque


def dfs(graph, source, path=None, explored=None):
    """Depth-First Search Recursive"""

    if not path:
        path = []

    if not explored:
        explored = set()

    explored.add(source)
    path.append(source)

    for node in graph[source]:
        if node not in explored:
            dfs(graph, node, path, explored)

    return path


def dfs_iterative(graph, source):
    explored = set()
    path = []
    stack = [source]

    while stack:
        v = stack.pop()

        if v not in explored:
            explored.add(v)
            path.append(v)
            stack.extend(graph[v])

    return path


def bfs(graph, source):
    """Breadth-First Search"""

    explored = {source}
    path = [source]
    queue = deque([source])

    while queue:
        v = queue.popleft()

        for tail in graph[v]:
            if tail not in explored:
                explored.add(tail)
                path.append(tail)
                queue.append(tail)

    return path
