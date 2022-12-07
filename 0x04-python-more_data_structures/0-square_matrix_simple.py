#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    f = []
    if not matrix:
        return None
    for row in matrix:
        f.append(list(map(lambda x: x**2, row)))
    return (f)
