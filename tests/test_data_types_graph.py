
"""Test Cases"""

from dataStructures.data_types_graph import dfs
from dataStructures.data_types_graph import dfs_iterative
from dataStructures.data_types_graph import bfs


def test_dfs_recursive():
    graph = {
        0: [1, 3, 4],
        1: [0, 2, 4],
        2: [1, 6],
        3: [0, 4, 6],
        4: [0, 1, 3, 5],
        5: [4],
        6: [2, 3]
    }

    path = dfs(graph, 0)
    assert path == [0, 1, 2, 6, 3, 4, 5]

def test_dfs_iterative():
    graph = {
        0: [1, 3, 4],
        1: [0, 2, 4],
        2: [1, 6],
        3: [0, 4, 6],
        4: [0, 1, 3, 5],
        5: [4],
        6: [2, 3]
    }

    path = dfs_iterative(graph, 0)
    assert path == [0, 4, 5, 3, 6, 2, 1]


def test_bfs():
    graph = {
        0: [1, 3, 4],
        1: [0, 2, 4],
        2: [1, 6],
        3: [0, 4, 6],
        4: [0, 1, 3, 5],
        5: [4],
        6: [2, 3]
    }

    path = bfs(graph, 0)
    assert path == [0, 1, 3, 4, 2, 6, 5]
