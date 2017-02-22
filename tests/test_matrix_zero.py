
"""Test Cases"""

from dataStructures.matrix_zero import matrix_zero


def test_matrix_zero():
    matrix = [
        [1, 2, 0, 4],
        [0, 3, 3, 3],
        [1, 2, 3, 4]
    ]

    matrix_zero(matrix)
    assert matrix == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 2, 0, 4]
    ]
