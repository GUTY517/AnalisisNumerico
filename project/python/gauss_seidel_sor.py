#! /usr/bin/env python3
'''Gauss Seidel SOR implementation'''

from math import sqrt
from copy import copy
from decimal import Decimal
from prettytable import PrettyTable
from numpy import diag, tril, triu, array, matmul
from numpy.linalg import det, matrix_power
from scipy import linalg as LA
import numpy as np


def gauss_sor(x_0, matrix, vector, w_value):
    '''Gauss SOR method'''
    answers = []
    new_x0 = copy(x_0)
    data_size = len(matrix)
    for i in range(data_size):
        results = 0
        for j in range(data_size):
            if j != i:
                results += matrix[i][j]*new_x0[j]
        results = (vector[i] - results)/matrix[i][i]
        relaxing = w_value*results + (1-w_value)*x_0[i]
        new_x0[i] = relaxing
        answers.append(relaxing)
    return answers


def norm_2(x_0, x_1):
    '''Returns Gauss Seidel SOR method using norm 2'''
    answer = 0
    data_size = len(x_0)
    for i in range(data_size):
        answer += (x_1[i]-x_0[i])**2
    error = sqrt(answer)
    return error

def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix


def main():
    '''Input data and excute code'''

    tolerance = float(input("Input tolerance: "))
    iterations = int(input("Input iterations: "))
    w_value = float(input("Input w_value: "))
    print("Input Matrix in one line")
    matrix = matrix_input()
    print("Input vector in one line")
    vector = matrix_input()
    print("Input x0 in one line")
    x_0 = matrix_input()

    data_size = len(matrix)
    determinant = det(matrix)
    if determinant == 0:
        return(1, "Determinant is ZERO (Multiple solutions)")

    diagonal_matrix = diag(diag(matrix))
    lower_matrix = diagonal_matrix - tril(matrix)
    upper_matrix = diagonal_matrix - triu(matrix)
    helper = diagonal_matrix - (w_value * lower_matrix)
    helper2 = ((1 - w_value) * diagonal_matrix) + (w_value * upper_matrix)

    power = matrix_power(helper, -1)
    t_matrix = matmul(power, helper2)

    transposed_matrix = [[abs(matrix[i][j])
                          for i in range(data_size)] for j in range(data_size)]
    helper3 = array(transposed_matrix)
    sum_columns = helper3.sum(axis=1)

    for i in range(data_size):
        diagonal_multiplication = (2*(transposed_matrix[i][i]))
        if all(diagonal_multiplication > sum_columns):
            spectral_checker = 1
        else:
            spectral_checker = 2

    if spectral_checker == 2:
        spectral_value = max(abs(LA.eigvals(t_matrix)))
        if spectral_value > 1:
            return (
                1, f"The spectral radio is larger than 1" /
                "({str(spectral_value)}). This method won't work.")

    title = ['Iterations']
    table_names = 0
    iterator = 0
    while table_names < len(x_0):
        title.append(f"x{str(table_names)}")
        table_names += 1
    title.append("Error")
    table = PrettyTable(title)
    table.add_row([iterator] + x_0 + ["-"])
    error = tolerance + 1
    while error > tolerance and iterator < iterations:
        x_1 = gauss_sor(x_0, matrix, vector, w_value)
        error = norm_2(x_0, x_1)
        iterator += 1
        table.add_row([iterator] + x_1 + ['%.2E' % Decimal(str(error))])
        x_0 = copy(x_1)

    return table



print(main())

### Test ###
# tolerance = 1e-7
# iterations = 100
# w_value = 1.5
# matrix = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
# vector = [1, 1, 1, 1]
# x_0 = [0, 0, 0, 0]
