#! /usr/bin/env python3
'''Gauss seidel method using numpy'''

from __future__ import print_function
import numpy as np
# from scipy.linalg import solve   #Uncomment if using last lines

def gauss_seidel():
    '''Gauss seidel method'''
    matrix_a = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])     #Change
    vector_b = [1.0, 2.0, 3.0]                                                      #Change
    guess = [1, 1, 1]                                                               #Change
    iterations = int(input("Input iterations: "))
    lower_triangle = np.tril(matrix_a)
    upper_triangle = matrix_a - lower_triangle

    for _ in range(iterations):
        guess = np.dot(np.linalg.inv(lower_triangle), vector_b - np.dot(upper_triangle, guess))
        # print("Iteration: ", i)                     #Uncomment if want to see the whole process
        # print(guess)                                #Uncomment if want to see the whole process
    return guess

print("Answer: ", gauss_seidel())


# matrix_a = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])     #Change
# vector_b = [1.0, 2.0, 3.0]                                                      #Change
# print("Answer: ", solve(matrix_a, vector_b))  #Solution using scipy
