#! /usr/bin/env python3
'''Vandermonde function'''

from numpy import vander
import numpy as np
import json
from flask_restful import Resource
from flask import request
from flask import abort


def swapping_lower(matrix, column, i):
    '''Return swapped numbers in lower matrix'''
    for j in range(0, i):
        if column[j] == 1:
            aux = matrix[j]
            matrix[j] = matrix[i]
            matrix[i] = aux
            break


def lower_triangular(matrix):
    '''Modified lower triangular matrix'''
    rows = len(matrix)
    columns = len(matrix[0])

    if rows == columns:
        variable_x = columns - 1
        variable_y = variable_x - 1
    else:
        variable_x = columns - 2
        variable_y = variable_x

    for i in range(variable_x, -1, -1):
        for j in range(variable_y, -1, -1):
            if i == j:
                column = [row[i] for row in matrix]
                if matrix[j][i] == 0:
                    for k in range(i - 1, -1, -1):
                        if 1 in column:
                            swapping_lower(matrix, column, i)
                            break
                        elif column[k] != 0:
                            aux = matrix[k]
                            matrix[k] = matrix[i]
                            matrix[i] = aux
                            break

                helper = matrix[i][j]
                if helper != 1:
                    if helper == 0:
                        return None
                    row = matrix[i]
                    length_rows = len(row)
                    for k in range(length_rows):
                        row[k] = row[k] / helper
                    matrix[i] = row
            else:
                helper = matrix[j][i]
                if helper != 0:
                    row1 = matrix[i]
                    row2 = matrix[j]
                    length_rows2 = len(row2)
                    for k in range(0, length_rows2):
                        row2[k] += ((-1 * helper) * row1[k])
                    matrix[j] = row2
    return matrix


def upper_triangular(matrix):
    '''Modified upper triangular matrix'''
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(columns):
        for j in range(i, rows):
            if i == j:
                column = [row[i] for row in matrix]
                length_columns = len(column)
                if matrix[i][i] == 0:
                    for k in range(i, length_columns):
                        if column[k] != 0:
                            aux = matrix[k]
                            matrix[k] = matrix[i]
                            matrix[i] = aux
                            break
                helper = matrix[i][j]
                if helper != 1:
                    if helper == 0:
                        return None
                    row = matrix[i]
                    length_rows = len(row)
                    for k in range(length_rows):
                        row[k] = row[k] / helper
                    matrix[i] = row

            else:
                helper = matrix[j][i]
                mult = helper / matrix[i][i]
                row1 = matrix[i]
                row2 = matrix[j]
                length_rows2 = len(row2)
                for k in range(0, length_rows2):
                    row2[k] -= (mult*row1[k])
                matrix[j] = row2
    return matrix


def polynomials(x_points, y_points):
    '''Returns polynomials values'''
    vandermonde_matrix = vander(x_points)
    vandermonde_matrix = vandermonde_matrix.tolist()
    augmented_matrix = (np.c_[vandermonde_matrix, y_points]).tolist()
    polynomial = upper_triangular(augmented_matrix)
    if polynomial is None:
        return None, None
    polynomial = lower_triangular(polynomial)
    if polynomial is None:
        return None, None
    return polynomial


def main(x_values, y_values):
    '''Method execution'''
    polynomial_values = polynomials(x_values, y_values)
    try:
        rounded_coefficients = [round(num, 4) for num in [item[-1] for item in polynomial_values]]
    except TypeError:
        abort(500, "There are two equal values in the table. Please fix this.")
    polynomial_text = "P(X)="
    data_size = len(rounded_coefficients)
    for i in range(data_size):
        if len(rounded_coefficients) - (i+1) == 1:
            polynomial_text += (f"{rounded_coefficients[i]}x")
        elif len(rounded_coefficients) - (i+1) == 0:
            if rounded_coefficients[i] >= 0:
                polynomial_text += (f"+{rounded_coefficients[i]}")
            else:
                polynomial_text += (f"{rounded_coefficients[i]}")
        else:
            if rounded_coefficients[i] >= 0:
                polynomial_text += (
                    f"+{rounded_coefficients[i]}x^{len(rounded_coefficients) - (i+1)}")
            else:
                polynomial_text += (
                    f"{rounded_coefficients[i]}x^{len(rounded_coefficients) - (i+1)}")
    polynomial_text = [polynomial_text]
    return vander(x_values), polynomial_text, rounded_coefficients

class Vandermonde(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        x_values = body_params["x_values"]
        y_values = body_params["y_values"]
        json_vander_table, json_polynomials, json_coefficients = main(x_values, y_values)
        json_data = json.loads(json.dumps({"VanderTable": json_vander_table.tolist(), "Polynomials": json_polynomials, "Coefficients": json_coefficients}))
        return json_data
