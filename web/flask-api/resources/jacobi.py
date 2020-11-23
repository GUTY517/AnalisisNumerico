#! /usr/bin/env python3
'''New Jacobi method implementation'''

import json
from math import sqrt
from copy import copy
import pandas as pd
from numpy.linalg import inv, det, LinAlgError
from flask_restful import Resource
from flask import request
from flask import abort


def jacobi(x_0, matrix, vector):
    '''Returns Jacobi answers'''
    answer = []
    data_size = len(matrix)
    for i in range(data_size):
        results = 0
        for j in range(data_size):
            if j != i:
                results += matrix[i][j]*x_0[j]
        results = (vector[i] - results)/matrix[i][i]
        answer.append(results)
    return answer


def norm_2(x_0, x_1):
    '''Returns vectors norm'''
    results = 0
    data_size = len(x_0)
    for i in range(data_size):
        results += ((x_1[i] - x_0[i])**2)
    try:
        if sqrt(results):
            error = sqrt(results)
            return error, 0
    except OverflowError:
        return 0, 1


def main(matrix, vector, x_0, tolerance, iterations):
    '''Returns Jacobi answer and calculation table'''
    determinant = det(matrix)
    if determinant == 0:
        abort(500, "Determinant is zero")
    try:
        inv(matrix)
    except LinAlgError:
        abort(500, "Matrix is not invertible")
    title = ['iterations']
    answer = 0
    iterator = 0
    while answer < len(x_0):
        title.append(f"x{str(answer)}")
        answer += 1
    title.append("Error")
    table = pd.DataFrame(columns=title)
    table = table.append(
        pd.Series([iterator] + x_0 + ["-"], index=table.columns), ignore_index=True)
    error = tolerance + 1
    jacobi_response = jacobi(x_0, matrix, vector)
    while error > tolerance and iterator < iterations:
        x_1 = jacobi(x_0, matrix, vector)
        answer = norm_2(x_0, x_1)
        error = answer[0]
        err = answer[1]
        if err == 1:
            abort(500, "Result is too big")
        iterator += 1
        table = table.append(
            pd.Series([iterator] + x_1 + [error], index=table.columns), ignore_index=True)
        x_0 = copy(x_1)

    return jacobi_response, table


class Jacobi(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]
        x_0 = body_params["x_0"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100
        if iterations <= 0:
            abort(500, "Inadequate iterations.")
        if tolerance <= 0:
            abort(500, "Inadequate tolerance.")
        answer, json_table = main(matrix, vector, x_0, tolerance, iterations)
        json_table = json.loads(json_table.to_json(orient="records"))
        json_data = json.loads(json.dumps({"Table": json_table, "Answers": answer}))
        return json_data
