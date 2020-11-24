#!/bin/python3
'''Cubic spline implementation'''

import json
import numpy as np
from numpy.linalg import det
from scipy.linalg import lu
from flask_restful import Resource
from flask import request
from flask import abort

def cubic_spline(data):
    '''Cubic spline method'''
    data_size = 4 * (len(data) - 1) + 1
    matrix = resulted_matrix(data, data_size)
    gen = matrix
    determinant = check_det(matrix)
    _, matrix = lu(matrix, permute_l=True)
    coefficients = [round(x, 4) for x in polynomial_values(matrix, len(matrix))]
    polynomials = clean_output(coefficients, data)
    return polynomials, gen


def resulted_matrix(data, data_size):
    '''Matrix creation by organizing and evaluating inputed data'''
    result = []
    row = list(np.zeros(data_size))
    row[0] = data[0][0]**3
    row[1] = data[0][0]**2
    row[2] = data[0][0]
    row[3] = 1
    row[data_size-1] = data[0][1]
    result.append(row)
    col = 0
    for i in range(1, len(data)):
        row = list(np.zeros(data_size))
        row[col] = data[i][0]**3
        row[col + 1] = data[i][0]**2
        row[col + 2] = data[i][0]
        row[col + 3] = 1
        row[data_size-1] = data[i][1]
        col += 4
        result.append(row)
    col = 0
    for i in range(1, len(data)-1):
        row = list(np.zeros(data_size))
        row[col] = data[i][0]**3
        row[col + 1] = data[i][0]**2
        row[col + 2] = data[i][0]
        row[col + 3] = 1
        row[col + 4] = -data[i][0]**3
        row[col + 5] = -data[i][0]**2
        row[col + 6] = -data[i][0]
        row[col + 7] = -1
        col += 4
        result.append(row)
    col = 0
    for i in range(1, len(data)-1):
        row = list(np.zeros(data_size))
        row[col] = 3 * (data[i][0] ** 2)
        row[col + 1] = 2 * data[i][0]
        row[col + 2] = 1
        row[col + 4] = -3 * (data[i][0] ** 2)
        row[col + 5] = -2 * data[i][0]
        row[col + 6] = -1
        col += 4
        result.append(row)
    col = 0
    for i in range(1, len(data)-1):
        row = list(np.zeros(data_size))
        row[col] = 6 * data[i][0]
        row[col + 1] = 2
        row[col + 4] = -6 * data[i][0]
        row[col + 5] = -2
        col += 4
        result.append(row)
    row = list(np.zeros(data_size))
    row[0] = 6 * data[0][0]
    row[1] = 2
    rown = list(np.zeros(data_size))
    rown[data_size-5] = 6 * data[len(data)-1][0]
    rown[data_size-4] = 2
    result.append(row)
    result.append(rown)
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
    '''Function to clean an organize the output'''
    results = []
    polynomials = []
    cont = 0
    for i in range(int(len(coefficients)/4)):
        results.append([i, coefficients[cont], coefficients[cont+1],
                        coefficients[cont+2], coefficients[cont+3]])
        cont += 4

    polynomials.append(["Polynomials", "Ranges"])
    data_size = len(results)
    for i in range(data_size):
        polynomial = f"P{i+1}="
        polynomial += str(results[i][1]) + "x^3 "
        if(results[i][2] < 0):
            polynomial += str(results[i][2])
        else:
            polynomial += "+" + str(results[i][2])
        polynomial += "x^2 "
        if(results[i][3] < 0):
            polynomial += str(results[i][3])
        else:
            polynomial += "+" + str(results[i][3])
        polynomial += "x "
        if(results[i][4] < 0):
            polynomial += str(results[i][4])
        else:
            polynomial += "+" + str(results[i][4])
        ranges = str(data[i][0]) + "<= x <= " + str(data[i+1][0])
        polynomials.append([polynomial, ranges])
    return polynomials


def check_det(matrix):
    '''Get matrix determinant and check if is zero'''
    data_size = len(matrix[0]) - 1
    square_matrix = [x[0:data_size] for x in matrix]
    if det(square_matrix) == 0:
        abort(500, "Matrix is not invertable.")
    return 0


class CubicSpline(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        x_values = body_params["x_values"]
        y_values = body_params["y_values"]
        data = list(map(lambda x, y: [x, y], x_values, y_values))
        polynomials, gen = cubic_spline(data)
        json_data = json.loads(json.dumps({"Table": gen, "Polynomials": polynomials}))
        return json_data
