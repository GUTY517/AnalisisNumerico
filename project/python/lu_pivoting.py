#! /usr/bin/env python3
'''LU Pivoting method implementation using scipy'''

import numpy as np
import scipy.linalg as la
from scipy.linalg import solve

def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix


def lu_pivoting():
    '''LU pivoting method'''
    matrix_a = np.array(matrix_input())
    matrix_b = np.array(matrix_input())

    augmented_matrix = np.append(matrix_a, matrix_b, axis=1)

    print("Matrix A:")
    print(matrix_a)
    print()
    print("Vector b:")
    print(matrix_b)
    print()
    print("Augmented matrix:")
    print(augmented_matrix)
    print()
    pivoted_matrix, triangular_matrix, solved_matrix = la.lu(matrix_a)
    print("Pivoted Matrix (P):")
    print(pivoted_matrix)
    print()
    print("Triangular matrix (L):")
    print(triangular_matrix)
    print()
    print("Solved matrix (U):")
    print(solved_matrix)
    print()
    print("Solved function using regression and progression:")
    print(solve(matrix_a, matrix_b))

lu_pivoting()


####### Tests #######
# matrix_a = np.array([[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]])
# matrix_b = np.array([[1], [1], [1], [1]])
