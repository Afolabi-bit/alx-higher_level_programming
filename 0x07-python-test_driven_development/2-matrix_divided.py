#!/usr/bin/python3

"""
matrix division module
"""

def matrix_divided(matrix, div):
    """
	matrix: must be a list of lists of int or floats
	div: number above zero
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if type(matrix) is not list:
         raise TypeError("matrix must be a matrix "
			 "(list of lists) of integers/floats")
    size = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix "
			    "(list of lists) of integers/floats")
        if size == 0:
            size == len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix "
			    "must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix "
				"(list of lists) of integers/floats")
    return list(map(lambda a: list(map(lambda b: round(b / div, 2), a)) , matrix.copy()))
