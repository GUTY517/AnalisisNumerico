#! /usr/bin/env python3
'''Gauss Seidel implementation using norm 2'''

import json
from math import sqrt
from copy import copy
import pandas as pd
from numpy.linalg import det, inv, LinAlgError
from flask_restful import Resource
from flask import request
from flask import abort


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


def main(tolerance, iterations, matrix, vector, x_0):
    '''Input variables and method execution'''

    determinant = det(matrix)
    if determinant == 0:
        abort(500, "Determinant is zero")
    try:
        inv(matrix)
    except LinAlgError:
        abort(500, "Is not possible to invert matrix")
    title = ['Iterations']
    table_tittles = 0
    iteration = 0
    while table_tittles < len(x_0):
        title.append(f"x{str(table_tittles)}")
        table_tittles += 1
    title.append("Error")
    table = pd.DataFrame(columns=title)
    table = table.append(pd.Series([iteration] + x_0 + ["-"], index=table.columns), ignore_index=True)
    error = tolerance + 1
    gauss_seidel_answer = gauss_seidel(x_0, matrix, vector)
    while error > tolerance and iteration < iterations:
        answers = gauss_seidel(x_0, matrix, vector)
        error = norm_2(x_0, answers)[0]
        iteration += 1
        table = table.append(pd.Series([iteration] + answers + [error], index=table.columns), ignore_index=True)
        x_0 = copy(answers)
    return gauss_seidel_answer, table


class GaussSeidel(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = body_params["matrix"]
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
        answer, json_table = main(tolerance, iterations, matrix, vector, x_0)
        json_table = json.loads(json_table.to_json(orient="records"))
        json_data =  json.loads(json.dumps({"Table": json_table, "Answer": answer}))
        return json_data
