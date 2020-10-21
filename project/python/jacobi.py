#! /usr/bin/env python3
"""Solves the equation Ax=vector_b via the Jacobi iterative method."""

from __future__ import print_function
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi():
    '''Jacobi implementation'''
    matrix_a = array([[2.0, 1.0], [5.0, 7.0]])  # Change
    vector_b = array([11.0, 13.0])            # Change
    guess_vector = array([1.0, 1.0])          # Change
    iterations = int(input("Number of iterations: "))

    # Create an initial guess if needed
    if guess_vector is None:
        guess_vector = zeros(len(matrix_a[0]))

    # Create a vector of the diagonal elements of matrix_a
    # and subtract them from matrix_a
    diagonal_matrix = diag(matrix_a)
    hollow_matrix = matrix_a - diagflat(diagonal_matrix)

    # Iterate for iterations times
    for _ in range(iterations):
        guess_vector = (vector_b - dot(hollow_matrix, guess_vector)) / diagonal_matrix
    print("Solved_matrix:\n")
    return guess_vector

pprint(jacobi())
