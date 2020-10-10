#! /usr/bin/env python3
'''Matrix pivoting'''

from __future__ import print_function
from numpy import array
import numpy as np
from scipy.linalg import lu


def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix

MATRIX = array(matrix_input())

PL, U = lu(MATRIX, permute_l=True)
print("\nPivoted matrix:\n", U)

# Example matrix array([[2,4,4,4],[1,2,3,3],[1,2,2,2],[1,4,3,4]])
