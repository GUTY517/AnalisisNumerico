#! /usr/bin/env python3
'''Method to calculate the pivoting matrix of a matrix'''

from __future__ import print_function
import pprint
import numpy as np


def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix


def pivot_matrix(matrix):
    '''Returns the pivoting matrix for matrix'''
    matrix = len(matrix)

    # Create an identity matrix, with floating point values
    id_mat = [[float(i == j) for i in range(matrix)] for j in range(matrix)]

    # Rearrange the identity matrix such that the largest element of
    # each column of matrix is placed on the diagonal of of matrix
    for j in range(matrix):
        row = max(range(j, matrix), key=lambda i: abs(matrix[i][j]))
        if j != row:
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]
    return id_mat


pprint.pprint(pivot_matrix(matrix_input()))


# Example matrix [[2,4,4,4],[1,2,3,3],[1,2,2,2],[1,4,3,4]]
