#!/usr/bin/python3
"""Creates a pascal triangle"""


def pascal_triangle(n):
    """pascal triangle to nth place"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    i = 0
    triangle = [[1], [1, 1]]
    for j in range(3, n + 1):
        row_n = [1]
        row_n.extend(triangle[-1][i] + triangle[-1][i+1] for i in range(j - 2))
        row_n.append(1)
        triangle.append(row_n)
    return triangle
