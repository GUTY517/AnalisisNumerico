#! /usr/bin/env python3
'''LU Pivoting method implementation using scipy'''

import numpy as np
import scipy.linalg as la

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
    pivoted_matrix, triangular_matrix, solved_matrix = la.lu(augmented_matrix)
    print("Dot matrix:")
    print(np.dot(triangular_matrix, solved_matrix))
    print()
    print("Pivoted Matrix:")
    print(pivoted_matrix)
    print()
    print("Triangular matrix:")
    print(triangular_matrix)
    print()
    print("Solved matrix:")
    print(solved_matrix)


lu_pivoting()


####### Tests #######
# augmented_matrix = np.array([[2, -3, 0, 1], [-4, 2, 0, -2], [1, 3, 0, 3], [-3, -1, 0, -1]]) #Det 0
# augmented_matrix = np.array([[2, -3, 5, 1], [-4, 2, 3, -2], [1, 3, 1, 3], [-3, -1, 9, -1]])
