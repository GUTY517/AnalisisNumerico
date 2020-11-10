#! /usr/bin/env python3
'''Jacobi SOR implementation'''

from decimal import Decimal
from numpy import linalg, diag, tril, triu, transpose, matmul, array
from scipy.linalg import eigvals
from prettytable import PrettyTable
import numpy as np


def jacobi_sor(matrix, vector, x_value, w_value, iterations, tolerance):
    '''Jacobi method'''
    title = ['Iteration']
    table_names = 0
    while table_names < len(x_value):
        title.append(f"x_value{str(table_names)}")
        table_names += 1

    title.append("Error")
    table = PrettyTable(title)

    data_size = len(matrix)
    determinant = linalg.det(matrix)
    if determinant == 0:
        return(1, "Determinant is ZERO")

    diagonal_matrix = diag(diag(matrix))
    lower_matrix = diagonal_matrix - tril(matrix)
    upper_matrix = diagonal_matrix - triu(matrix)
    helper = diagonal_matrix - (w_value * lower_matrix)
    helper2 = ((1 - w_value) * diagonal_matrix) + (w_value * upper_matrix)

    power = linalg.matrix_power(helper, -1)
    t_matrix = matmul(power, helper2)
    relaxed = transpose(vector) * w_value
    sor_answer = matmul(power, relaxed)

    transposed_matrix = array(
        [[abs(matrix[i][j]) for i in range(data_size)] for j in range(data_size)])
    sum_columns = transposed_matrix.sum(axis=1)

    for i in range(data_size):
        diagonal_multiplication = (2*(transposed_matrix[i][i]))
        if all(diagonal_multiplication > sum_columns):
            spectral_checker = 1
        else:
            spectral_checker = 2

    if spectral_checker == 2:
        spectral_value = max(abs(eigvals(t_matrix)))
        if spectral_value > 1:
            return (
                1, f"The spectral radio is larger than 1" / \
                    "({str(spectral_value)}). This method won't work")
        spectral_checker = 1

    if spectral_checker == 1:
        counter = 0
        table.add_row([counter] + x_value + ["-"])
        x_value = transpose(x_value)
        new_tolerance = tolerance + 1
        while counter < iterations and new_tolerance > tolerance:
            x_n = (matmul(t_matrix, x_value)) + sor_answer
            tolerance = linalg.norm(x_n - x_value)
            counter += 1
            table.add_row([counter] + x_n.tolist() + ['%.2E' %
                                                      Decimal(str(tolerance))])
            x_value = x_n
    print("Spectral value: ", max(abs(eigvals(t_matrix))))
    print("Answer (C): ", sor_answer)
    return table


def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix

def main():
    '''Value input and method execution'''
    tolerance = float(input("Input tolerance: "))
    iterations = int(input("Input iterations: "))
    w_value = float(input("Input W value: "))
    print("Input matrix in one line")
    matrix = matrix_input()
    print("Input vector in one line")
    vector = matrix_input()
    print("Input x0 in one line")
    x_0 = matrix_input()
    return jacobi_sor(matrix, vector, x_0, w_value, iterations, tolerance)


print(main())

### Test ###
# tolerance = 1e-7
# iterations = 100
# w_value = 1.5
# matrix_a = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
# vector = [1, 1, 1, 1]
# x_0 = [0, 0, 0, 0]
