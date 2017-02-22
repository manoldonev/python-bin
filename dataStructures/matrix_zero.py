
"""Matrix Zero-Setter Package"""


def matrix_zero(matrix):
    """Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column is set to 0."""
    # O(n^2) time, O(m+n) space
    m = len(matrix)
    if m == 0:
        return matrix

    n = len(matrix[0])

    rows_to_delete = set()
    cols_to_delete = set()
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 0:
                rows_to_delete.add(i)
                cols_to_delete.add(j)
                break

    for i in range(0, m):
        for j in range(0, n):
            if i in rows_to_delete or j in cols_to_delete:
                matrix[i][j] = 0
