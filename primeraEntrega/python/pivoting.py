#! /usr/bin/env python3

from numpy import array
from scipy.linalg import lu


def matrix_input():
    '''Console matrix input'''
    while True:
        try:
            r = int(input("Matrix A rows: "))
            if r < 1:
                raise ValueError
        except ValueError:
            print("Not a valid input.")
        else:
            break
    while True:
        try:
            c = int(input("Matrix A columns: "))
            if c < 1:
                raise ValueError
        except ValueError:
            print("Not a valid input.")
        else:
            break
    result = np.zeros((r, c), dtype=np.double)
    for i in range(r):
        for j in range(c):
            while True:
                try:
                    result[i][j] = np.double(
                        input("[" + str(i) + "][" + str(j) + "] = "))
                except ValueError:
                    print("Not a valid input.")
                else:
                    break
    return result

a = array(matrix_input())

pl, u = lu(a, permute_l=True)
print(u)

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
#         print(u'\u250c'+u'\u2500'*w+u'\u2510')
#         for AA in A:
#             print(' ', end='')
#             print('[', end='')
#             for i, AAA in enumerate(AA[:-1]):
#                 w1 = max([len(str(s)) for s in A[:, i]])
#                 print(str(AAA)+' '*(w1-len(str(AAA))+1), end='')
#             w1 = max([len(str(s)) for s in A[:, -1]])
#             print(str(AA[-1])+' '*(w1-len(str(AA[-1]))), end='')
#             print(']')
#         print(u'\u2514'+u'\u2500'*w+u'\u2518')


# def matrix_input():
#     '''Console matrix input'''
#     while True:
#         try:
#             r = int(input("Matrix A rows: "))
#             if r < 1:
#                 raise ValueError
#         except ValueError:
#             print("Not a valid input.")
#         else:
#             break
#     while True:
#         try:
#             c = int(input("Matrix A columns: "))
#             if c < 1:
#                 raise ValueError
#         except ValueError:
#             print("Not a valid input.")
#         else:
#             break
#     result = np.zeros((r, c), dtype=np.double)
#     for i in range(r):
#         for j in range(c):
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
#           c = matrix[i][j]/matrix[j][j]
#           matrix[i] = [matrix[i][k]-c*matrix[j][k] for k in range(n)]
#     return pprint(np.asarray(matrix))

# matrix_input()