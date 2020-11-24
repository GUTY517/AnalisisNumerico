#! /usr/bin/env python3
'''Linear spline implementation'''

import json
import numpy as np
from numpy.linalg import det
from scipy.linalg import lu
from flask_restful import Resource
from flask import request
from flask import abort


def lineal_spline(data):
    '''Linear spline method'''
    data_size = 2 * (len(data) - 1) + 1
    matrix = resulted_matrix(data, data_size)
    gen = matrix
    determinant = check_det(matrix)
    _, matrix = lu(matrix, permute_l=True)
    coefficients = [round(x, 4) for x in polynomial_values(matrix.tolist(), len(matrix))]
    polynomials = clean_output(coefficients, data)
    return polynomials, gen


def resulted_matrix(data, data_size):
    '''Matrix creation by organizing and evaluating inputed data'''
    result = []
    row = list(np.zeros(data_size))
    row[0] = data[0][0]
    row[1] = 1
    row[data_size-1] = data[0][1]
    result.append(row)
    column = 0
    for i in range(1, len(data)):
        row = list(np.zeros(data_size))
        row[i-1 + column] = data[i][0]
        row[i + column] = 1
        row[data_size-1] = data[i][1]
        column += 1
        result.append(row)
    column = 0
    for j in range(1, len(data) - 1):
        row = list(np.zeros(data_size))
        row[column] = data[j][0]
        row[column + 1] = 1
        row[column + 2] = -data[j][0]
        row[column + 3] = -1
        column += 2
        result.append(row)
    return result


def polynomial_values(matrix, data_size):
    '''Get polynomial values'''
    vector = [0] * data_size
    vector[data_size-1] = matrix[data_size-1][data_size] / \
        matrix[data_size-1][data_size-1]
    i = data_size-2
    while i >= 0:
        result = 0
        counter = len(vector)-1
        while counter >= 0:
            result += (matrix[i][counter]*vector[counter])
            counter -= 1
        vector[i] = (matrix[i][data_size]-result)/matrix[i][i]
        i -= 1
    return vector


def clean_output(coefficients, data):
    '''Function to clean and organize the output'''
    results = []
    polynomials = []
    cont = 0
    for i in range(int(len(coefficients)/2)):
        results.append([i, coefficients[cont], coefficients[cont+1]])
        cont += 2

    polynomials.append(["Polynomials", "Ranges"])
    data_size = len(results)
    for i in range(data_size):
        polynomial = f'P{i+1}='
        polynomial += str(results[i][1]) + "x "
        if results[i][2] < 0:
            polynomial += str(results[i][2])
        else:
            polynomial += "+" + str(results[i][2])
        ranges = str(data[i][0]) + "<= x <= " + str(data[i+1][0])
        polynomials.append([polynomial, ranges])
    return polynomials


def check_det(data):
    '''Get matrix determinant and check if is zero'''
    data_size = len(data[0]) - 1
    square_a = [x[0:data_size] for x in data]
    if det(square_a) == 0:
        abort(500, "Resulted matrix is not invertable, Determinant is zero")
    return 0


class LinealSpline(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        x_values = body_params["x_values"]
        y_values = body_params["y_values"]
        data = list(map(lambda x, y: [x, y], x_values, y_values))
        polynomials, gen = lineal_spline(data)
        json_data = json.loads(json.dumps({"Table": gen, "Polynomials": polynomials}))
        return json_data
