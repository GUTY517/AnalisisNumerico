#! /usr/bin/env python3
'''Jacobi SOR implementation'''

from decimal import Decimal
from numpy import linalg, diag, tril, triu, transpose, matmul, array
from scipy.linalg import eigvals
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request


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
            new_tolerance = linalg.norm(x_n - x_value)
            counter += 1
            table.add_row([counter] + x_n.tolist() + ['%.2E' %
                                                      Decimal(str(new_tolerance))])
            x_value = x_n
    return table, sor_answer, max(abs(eigvals(t_matrix))))


class JacobiSor(Resource):

    def post(self):
        body_params = request.get_json()
        matrix = body_params["matrix"]
        w_value = body_params["w_value"]
        vector = body_params["vector"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        x_0 = body_params["x_0"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100
        json_table, _, _ = jacobi_sor(tolerance, iterations, w_value, matrix, vector, x_0)
        return json_table
