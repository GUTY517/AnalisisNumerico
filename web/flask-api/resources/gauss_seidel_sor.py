#! /usr/bin/env python3
'''Gauss Seidel SOR implementation'''

import json
from math import sqrt
from copy import copy
from decimal import Decimal
import pandas as pd
from numpy import diag, tril, triu, transpose, array, matmul
from numpy.linalg import det, matrix_power
from scipy import linalg as LA
from flask_restful import Resource
from flask import request
from flask import abort


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


def main(matrix, vector, x_0, w_value, iterations, tolerance):
    '''Input data and execute code'''

    data_size = len(matrix)
    determinant = det(matrix)
    if determinant == 0:
        abort(500, "Determinant is zero")

    diagonal_matrix = diag(diag(matrix))
    lower_matrix = diagonal_matrix - tril(matrix)
    upper_matrix = diagonal_matrix - triu(matrix)
    helper = diagonal_matrix - (w_value * lower_matrix)
    helper2 = ((1 - w_value) * diagonal_matrix) + (w_value * upper_matrix)

    power = matrix_power(helper, -1)
    t_matrix = matmul(power, helper2)
    relaxed = transpose(vector) * w_value
    sor_answer = matmul(power, relaxed)

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
            abort(
                500, f"The spectral radio is larger than 1" /
                "({str(spectral_value)}). This method won't work.")

    title = ['Iterations']
    table_names = 0
    iterator = 0
    while table_names < len(x_0):
        title.append(f"x{str(table_names)}")
        table_names += 1
    title.append("Error")
    table = pd.DataFrame(columns=title)
    table = table.append(pd.Series([iterator] + x_0 + ["-"], index=table.columns), ignore_index=True)
    error = tolerance + 1
    while error > tolerance and iterator < iterations:
        x_1 = gauss_sor(x_0, matrix, vector, w_value)
        error = norm_2(x_0, x_1)
        iterator += 1
        table = table.append(pd.Series([iterator] + x_1 + ['%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
        x_0 = copy(x_1)

    return sor_answer, table, max(abs(LA.eigvals(t_matrix)))


class GaussSeidelSor(Resource):
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
        answer, json_table, spectral_value = main(matrix, vector, x_0, w_value, iterations, tolerance)
        json_table = json.loads(json_table.to_json(orient="records"))
        json_data = json.loads(json.dumps({"Table":json_table, "Answers": answer.tolist(), "SpectralValue": [spectral_value]}))
        return json_data
