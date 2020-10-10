#! /usr/bin/env python3
'''Matrix pivoting'''

from __future__ import print_function
from numpy import array
import numpy as np
from scipy.linalg import lu


def matrix_input():
    '''Console matrix input'''
    while True:
        try:
            row = int(input("Matrix A rows: "))
            if row < 1:
                raise ValueError
        except ValueError:
            print("Not a valid input.")
        else:
            break
    while True:
        try:
            colums = int(input("Matrix A columns: "))
            if colums < 1:
                raise ValueError
        except ValueError:
            print("Not a valid input.")
        else:
            break
    result = np.zeros((row, colums), dtype=np.double)
    for i in range(row):
        for j in range(colums):
            while True:
                try:
                    result[i][j] = np.double(
                        input("[" + str(i) + "][" + str(j) + "] = "))
                except ValueError:
                    print("Not a valid input.")
                else:
                    break
    return result

MATRIX = array(matrix_input())

PL, U = lu(MATRIX, permute_l=True)
print(U)

# Example matrix array([[2,4,4,4],[1,2,3,3],[1,2,2,2],[1,4,3,4]])

# Gauss method without libraries

# '''Basic pivoting using gauss method'''

# from __future__ import print_function
# import numpy as np


# def pprint(A):
#     '''Pretty print method to output the resulted matrix in console'''
#     if A.ndim == 1:
#         print(A)
#     else:
#         w = max([len(str(s)) for s in A])
#         print("\nPivoted matrix:\n")
#         print(U'\u250c'+U'\u2500'*w+U'\u2510')
#         for AA in A:
#             print(' ', end='')
#             print('[', end='')
#             for i, AAA in enumerate(AA[:-1]):
#                 w1 = max([len(str(s)) for s in A[:, i]])
#                 print(str(AAA)+' '*(w1-len(str(AAA))+1), end='')
#             w1 = max([len(str(s)) for s in A[:, -1]])
#             print(str(AA[-1])+' '*(w1-len(str(AA[-1]))), end='')
#             print(']')
#         print(U'\u2514'+U'\u2500'*w+U'\u2518')


# def matrix_input():
#     '''Console matrix input'''
#     while True:
#         try:
#             row = int(input("Matrix A rows: "))
#             if row < 1:
#                 raise ValueError
#         except ValueError:
#             print("Not a valid input.")
#         else:
#             break
#     while True:
#         try:
#             colums = int(input("Matrix A columns: "))
#             if colums < 1:
#                 raise ValueError
#         except ValueError:
#             print("Not a valid input.")
#         else:
#             break
#     result = np.zeros((row, colums), dtype=np.double)
#     for i in range(row):
#         for j in range(colums):
#             while True:
#                 try:
#                     result[i][j] = np.double(
#                         input("[" + str(i) + "][" + str(j) + "] = "))
#                 except ValueError:
#                     print("Not a valid input.")
#                 else:
#                     break
#     gausselim2(result)


# def gausselim2(matrix):
#     '''Gauss pivoting method'''
#     m = len(matrix); n = len(matrix[0])
#     for j in range(min(n,m)):
#        if(matrix[j][j]==0):
#           column = [matrix[k][j] for k in range(j,m)]
#           pivot = column.index(max(column))
#           temp = matrix[j]; matrix[j] = matrix[pivot]; matrix[pivot] = temp
#        for i in range(j+1,m):
#           colums = matrix[i][j]/matrix[j][j]
#           matrix[i] = [matrix[i][k]-colums*matrix[j][k] for k in range(n)]
#     return pprint(np.asarray(matrix))

# matrix_input()
