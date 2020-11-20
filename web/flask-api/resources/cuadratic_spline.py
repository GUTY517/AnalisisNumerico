#!/bin/python3
'''Cuadratic spline method'''

import numpy as np
import json
from numpy.linalg import det
from scipy.linalg import lu
from flask_restful import Resource
from flask import request


def cuadratic_spline(data):
    '''Cuadratic spline method'''
    data_size = 3 * (len(data) - 1) + 1
    matrix = resulted_matrix(data, data_size)
    gen = matrix
    determinant = check_det(matrix)
    if determinant[0] == 1:
        return determinant
    _, matrix = lu(matrix, permute_l=True)
    coefficients = polynomial_values(matrix.tolist(), len(matrix))
    polynomials = clean_output(coefficients, data)
    return (0, polynomials, gen)


def resulted_matrix(data, data_size):
    '''Matrix creation by organizing and evaluating inputed data'''
    result = []
    row = list(np.zeros(data_size))
    row[0] = data[0][0]**2
    row[1] = data[0][0]
    row[2] = 1
    row[data_size-1] = data[0][1]
    result.append(row)
    column = 0
    for i in range(1, len(data)):
        row = list(np.zeros(data_size))
        row[column] = data[i][0]**2
        row[column + 1] = data[i][0]
        row[column + 2] = 1
        row[data_size-1] = data[i][1]
        column += 3
        result.append(row)
    column = 0
    for i in range(1, len(data)-1):
        row = list(np.zeros(data_size))
        row[column] = data[i][0]**2
        row[column + 1] = data[i][0]
        row[column + 2] = 1
        row[column + 3] = -data[i][0]**2
        row[column + 4] = -data[i][0]
        row[column + 5] = -1
        column += 3
        result.append(row)
    column = 0
    for i in range(1, len(data)-1):
        row = list(np.zeros(data_size))
        row[column] = 2 * data[i][0]
        row[column + 1] = 1
        row[column + 3] = -2 * data[i][0]
        row[column + 4] = -1
        column += 3
        result.append(row)
    row = list(np.zeros(data_size))
    row[0] = 1
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
    '''Function to clean an organize the output'''
    results = []
    polynomials = []
    cont = 0
    for i in range(int(len(coefficients)/3)):
        results.append(
            [i, coefficients[cont], coefficients[cont+1], coefficients[cont+2]])
        cont += 3

    polynomials.append(["Polynomials", "Ranges"])
    data_size = len(results)
    for i in range(data_size):
        polynomial = f"P{i+1}="
        polynomial += str(results[i][1]) + "x^2 "
        if(results[i][2] < 0):
            polynomial += str(results[i][2])
        else:
            polynomial += "+" + str(results[i][2])
        polynomial += "x "
        if(results[i][3] < 0):
            polynomial += str(results[i][3])
        else:
            polynomial += "+" + str(results[i][3])
        ranges = str(data[i][0]) + "<= x <= " + str(data[i+1][0])
        polynomials.append([polynomial, ranges])
    return polynomials


def check_det(matrix):
    '''Get matrix determinant and check if is zero'''
    data_size = len(matrix[0]) - 1
    square_a = [x[0:data_size] for x in matrix]
    if det(square_a) == 0:
        return(
            1, '"The generated matrix is not invertible. '
            'You may want to select a different set of points')
    return(0, "OK")


class cuadratic_spline(Resources):

    def post(self):
        body_params = request.get_json()
        data = body_params["table"]
        _, polynomials, gen = cuadratic_spline(data)
        json_data = json.dumps(polynomials, gen)
        return json_data
