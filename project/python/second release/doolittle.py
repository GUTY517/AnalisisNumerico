#! /usr/bin/env python3
'''Doolittle method implemented in numpy'''

import numpy as np
from scipy.linalg import solve


def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix


def doolittle(matrix):
    '''Doolittle implementation using numpy'''
    matrix_size = matrix.shape[0]
    upper_triangular_matrix = np.zeros((matrix_size, matrix_size), dtype=np.double)
    lower_triangular_matrix = np.eye(matrix_size, dtype=np.double)

    for k in range(matrix_size):
        upper_triangular_matrix[k, k:] = matrix[k, k:] - \
            lower_triangular_matrix[k, :k] @ upper_triangular_matrix[:k, k:]
        lower_triangular_matrix[(k+1):, k] = (matrix[(k+1):, k] - lower_triangular_matrix[(
            k+1):, :] @ upper_triangular_matrix[:, k]) / upper_triangular_matrix[k, k]
    return lower_triangular_matrix, upper_triangular_matrix


def main():
    '''Function output'''
    matrix = matrix_input()
    vector = matrix_input()
    lower_triangular_matrix, upper_triangular_matrix = doolittle(matrix)

    print("Lower triangular matrix (L)")
    print(lower_triangular_matrix)
    print()
    print("Upper triangular matrix (U)")
    print(upper_triangular_matrix)
    print()
    print("Solved function using regression and progression:")
    print(solve(matrix, vector))


main()

### Tests ###
# matrix = np.array([[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]])
# vector = np.array([[1], [1], [1], [1]])
