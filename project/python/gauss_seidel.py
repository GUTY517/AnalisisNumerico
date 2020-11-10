#! /usr/bin/env python3
'''Gauss Seidel implementation using norm 2'''

from math import sqrt
from copy import copy
import numpy as np
from prettytable import PrettyTable
from numpy.linalg import det, inv, LinAlgError


def gauss_seidel(x_0, matrix, vector):
    '''Gauss Seidel method'''
    answers = []
    new_x0 = copy(x_0)
    data_size = len(matrix)
    for i in range(data_size):
        results = 0
        for j in range(data_size):
            if j != i:
                results += matrix[i][j]*new_x0[j]
        results = (vector[i] - results)/matrix[i][i]
        new_x0[i] = results
        answers.append(results)
    return answers


def norm_2(x_0, x_1):
    '''Returns Gauss Seidel method using norm 2'''
    answer = 0
    data_size = len(x_0)
    for i in range(data_size):
        answer += ((x_1[i] - x_0[i])**2)
    try:
        if sqrt(answer):
            error = sqrt(answer)
            return error, 0
    except OverflowError:
        return 0, 1


def matrix_input():
    '''Console matrix_a input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix


def main():
    '''Input variables and method execution'''
    tolerance = float(input("Input tolerance: "))
    iterations = int(input("Input iterations: "))
    print("Input matrix in one line")
    matrix = matrix_input()
    print("Input vector in one line")
    vector = matrix_input()
    print("Input x0 in one line")
    x_0 = matrix_input()

    determinant = det(matrix)
    if determinant == 0:
        return(1, "Determinant is ZERO (no unique solution)")

    try:
        inv(matrix)
    except LinAlgError:
        return(1, "The matrix is not invertible")

    title = ['Iterations']
    table_tittles = 0
    iteration = 0
    while table_tittles < len(x_0):
        title.append(f"x{str(table_tittles)}")
        table_tittles += 1

    title.append("Error")
    table = PrettyTable(title)
    table.add_row([iteration] + x_0 + ["-"])
    error = tolerance + 1
    gauss_seidel_answer = gauss_seidel(x_0, matrix, vector)
    while error > tolerance and iteration < iterations:
        answers = gauss_seidel(x_0, matrix, vector)
        error = norm_2(x_0, answers)[0]
        iteration += 1
        table.add_row([iteration] + answers + [error])
        x_0 = copy(answers)
    print(gauss_seidel_answer)
    return table


print(main())

### Tests ###
# tolerance = 1e-7
# x_0 = [0, 0, 0, 0]
# iterations = 100
# matrix = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
# vector = [1, 1, 1, 1]
# print(main())
