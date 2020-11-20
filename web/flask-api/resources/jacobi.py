#! /usr/bin/env python3
'''New Jacobi method implementation'''

from math import sqrt
from copy import copy
from prettytable import PrettyTable
from numpy.linalg import inv, det, LinAlgError
from flask_restful import Resource
from flask import request


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

def main(tolerance, iterations, matrix, vector, x_0):
    '''Returns Jacobi answer and calculation table'''

    determinant = det(matrix)
    if determinant == 0:
        return(1, "Determinant is zero")
    try:
        inv(matrix)
    except LinAlgError:
        return 1, "Matrix is not invertible"

    title = ['iterations']
    answer = 0
    iterator = 0
    while answer < len(x_0):
        title.append(f"x{str(answer)}")
        answer += 1
    title.append("Error")
    table = PrettyTable(title)
    table.add_row([iterator] + x_0 + ["-"])
    error = tolerance + 1
    jacobi_response = jacobi(x_0, matrix, vector)
    while error > tolerance and iterator < iterations:
        x_1 = jacobi(x_0, matrix, vector)
        answer = norm_2(x_0, x_1)
        error = answer[0]
        err = answer[1]
        if err == 1:
            return 1, "Result is too big"
        iterator += 1
        table.add_row([iterator] + x_1 + [error])
        x_0 = copy(x_1)

    return jacobi_response, table

class Jacobi(Resource):

    def post(self):
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
        _, json_table = main(tolerance, iterations, matrix, vector, x_0)
        return json_table
