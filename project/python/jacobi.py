#! /usr/bin/env python3
"""Solves the equation Ax=vector_b via the Jacobi iterative method."""

from __future__ import print_function
import numpy as np
# from scipy.linalg import solve   #Uncomment if using last lines

def jacobi():
    '''Jacobi method using numpy'''
    matrix_a = np.array(
        [[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])  # Change
    vector_b = [1.0, 2.0, 3.0]                                   # Change
    guess = [1.0, 1.0, 1.0]                                      # Change
    iterations = int(input("Input iterations: "))
    diagonal_matrix = np.diag(matrix_a)
    hollow_matrix = matrix_a - np.diagflat(diagonal_matrix)

    for _ in range(iterations):
        guess = (vector_b - np.dot(hollow_matrix, guess)) / diagonal_matrix
        # print("Iteration: ", i)                     #Uncomment if want to see the whole process
        # print(guess)                                #Uncomment if want to see the whole process
    return guess

print("Answer: ", jacobi())

# matrix_a = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])  # Change
# vector_b = [1.0, 2.0, 3.0]                                   # Change
# print("Answer: ", solve(matrix_a, vector_b))
