#! /usr/bin/env python3
'''Web implementation of partial matrix pivoting'''

from __future__ import print_function
import json
import numpy as np
from scipy.linalg import lu
from numpy import linalg as la
from flask_restful import Resource
from flask import request
from flask import abort


def stepped_matrix(matrix, vector):
    '''Return the stepped matrix'''

    if la.det(matrix) == 0:
        abort(500, "Determinant is zero")
    try:
        la.inv(matrix)
    except la.LinAlgError:
        abort(500, "Matrix cannot be inverted")
    augmented_matrix = np.append(matrix, vector, axis=1)
    matrix_size = len(augmented_matrix)
    for i in range(0, matrix_size):
        for j in range(i, matrix_size):
            if i == j:
                column = [row[i] for row in augmented_matrix]
                column_len = len(column)
                if augmented_matrix[i][i] == 0:
                    for k in range(i, column_len):
                        if column[k] != 0:
                            aux = augmented_matrix[k]
                            augmented_matrix[k] = augmented_matrix[i]
                            augmented_matrix[i] = aux
                            break

                if augmented_matrix[i][i] == 0:
                    abort(500, "Matrix cannot be augmented")
            else:
                mult = augmented_matrix[j][i] / augmented_matrix[i][i]
                row1 = augmented_matrix[i]
                row2 = augmented_matrix[j]
                data_size = len(row2)
                for k in range(0, data_size):
                    row2[k] -= (mult * row1[k])
                augmented_matrix[j] = row2
    return augmented_matrix


def get_values(step_matrix, matrix_size):
    '''Returns x values (answers)'''
    x_values = []
    for _ in range(matrix_size):
        x_values.append(0)
    x_values[matrix_size - 1] = step_matrix[matrix_size - 1][matrix_size] / \
        step_matrix[matrix_size - 1][matrix_size - 1]
    i = matrix_size - 2
    while i >= 0:
        result = 0
        data_size = len(x_values) - 1
        while data_size >= 0:
            result += (step_matrix[i][data_size] * x_values[data_size])
            data_size -= 1
        x_values[i] = (step_matrix[i][matrix_size] - result) / step_matrix[i][i]
        i -= 1
    return x_values


def partial_pivoting(matrix, vector):
    '''Main function partial pivoting'''
    augmented_matrix = np.append(matrix, vector, axis=1)
    _, pivoted_matrix = lu(augmented_matrix, permute_l=True)
    results_x = get_values(stepped_matrix(matrix, vector), len(augmented_matrix))
    return pivoted_matrix, results_x


class PartialPivoting(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]
        pivoted_matrix, x_values = partial_pivoting(matrix, vector)
        json_data = json.loads(json.dumps(pivoted_matrix.tolist() + x_values))
        return json_data
