#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ squares each entry of a
        matrix individually """
    a = list(map(lambda sub: list(map(lambda e: e ** 2, sub)), matrix))
    return a
