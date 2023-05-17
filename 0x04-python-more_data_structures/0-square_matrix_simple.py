#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for item in matrix:
        new = [new_matrix ** 2 for new_matrix in item]
        mat.append(new)
    return mat
