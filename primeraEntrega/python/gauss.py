#! /usr/bin/env python3
'''Script to calculate pivot matrix using gauss method'''

from __future__ import print_function
import numpy as np
import numpy.linalg

def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix

def gauss(matrix):
    '''Gaus method using numpy'''
    identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    return numpy.linalg.solve(matrix, identity_matrix)

print(gauss(matrix_input()))
