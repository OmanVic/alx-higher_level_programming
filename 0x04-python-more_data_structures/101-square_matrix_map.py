#!/usr/bin/python3
def square_matrix_map(matrix=[]):
     return [list(map(lambda i: i * i, mat)) for mat in matrix]
