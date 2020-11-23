#! /usr/bin/env python3
'''Jacobi SOR implementation'''

import json
from decimal import Decimal
import pandas as pd
from numpy import linalg, diag, tril, triu, transpose, matmul, array
from scipy.linalg import eigvals
from flask_restful import Resource
from flask import request
from flask import abort


def jacobi_sor(matrix, vector, x_0, w_value, iterations, tolerance):
    '''Jacobi method'''
    title = ['Iteration']
    table_names = 0
    while table_names < len(x_0):
        title.append(f"x_0{str(table_names)}")
        table_names += 1
    title.append("Error")
    table = pd.DataFrame(columns=title)
    data_size = len(matrix)
    determinant = linalg.det(matrix)
    if determinant == 0:
        abort(500, "Determinant is zero")

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
            abort(
                500, f"The spectral radio is larger than 1" /
                "({str(spectral_value)}). This method won't work")
        spectral_checker = 1
    if spectral_checker == 1:
        counter = 0
        table = table.append(
            pd.Series([counter] + x_0 + ["-"], index=table.columns), ignore_index=True)
        x_0 = transpose(x_0)
        new_tolerance = tolerance + 1
        while counter < iterations and new_tolerance > tolerance:
            x_n = (matmul(t_matrix, x_0)) + sor_answer
            new_tolerance = linalg.norm(x_n - x_0)
            counter += 1
            table = table.append(pd.Series([counter] + x_n.tolist() + ['%.2E' %
                                                                       Decimal(str(new_tolerance))], index=table.columns), ignore_index=True)
            x_0 = x_n
    return sor_answer, table, max(abs(eigvals(t_matrix)))


class JacobiSor(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
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
        if iterations <= 0:
            abort(500, "Inadequate iterations.")
        if tolerance <= 0:
            abort(500, "Inadequate tolerance.")
        answer, json_table, spectral_values = jacobi_sor(
            matrix, vector, x_0, w_value, iterations, tolerance)
        json_data = (json.loads(json_table.to_json(orient="records")
                                ) + answer.tolist() + [spectral_values])
        return json_data
