#! /usr/bin/env python3

''' lower_upper_matrix Gaus method using scipy'''

import numpy as np
from scipy.linalg import lu
from scipy.linalg import lu_factor, lu_solve


def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix


def lu_gauss():
    '''lower_upper_matrix Gauss method'''
    matrix_a = np.array(matrix_input())
    vector = np.array(matrix_input())

    augmented_matrix = np.append(matrix_a, vector, axis=1)

    print("Matrix A:")
    print(matrix_a)
    print()
    print("Vector:")
    print(vector)
    print()
    print("Augmented matrix:")
    print(augmented_matrix)
    print()
    permuted_matrix, lower_triangular_matrix, upper_triangular_matrix = lu(
        matrix_a)
    print("Permuted matrix (P):")
    print(permuted_matrix)
    print()
    print("Lower triangular matrix (L):")
    print(lower_triangular_matrix)
    print()
    print("Upper triangular matrix (U):")
    print(upper_triangular_matrix)
    print()
    lower_upper_matrix, pivoted_indices = lu_factor(matrix_a)
    print("Solved function using regression and progression:")
    print(lu_solve((lower_upper_matrix, pivoted_indices), vector))


lu_gauss()

### Tests ###
# matrix_a = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
# vector = [[1], [1], [1], [1]]
