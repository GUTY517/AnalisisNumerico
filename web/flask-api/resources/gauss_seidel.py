#! /usr/bin/env python3
'''Gauss Seidel implementation using norm 2'''

from math import sqrt
from copy import copy
from prettytable import PrettyTable
from numpy.linalg import det, inv, LinAlgError
from flask_restful import Resource
from flask import request


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
    return table, gauss_seidel_answer


class GaussSeidel(Resource):

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
        json_table, _ = main(tolerance, iterations, matrix, vector, x_0)
        return json_table
