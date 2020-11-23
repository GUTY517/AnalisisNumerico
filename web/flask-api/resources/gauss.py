#! /usr/bin/env python3
'''Gauss web implementation'''

from __future__ import print_function
import json
import numpy as np
from flask_restful import Resource
from flask import request
from numpy import linalg as la
from flask import abort


def stepped_matrix(matrix, vector):
    '''Returns stepped matrix'''
    if la.det(matrix) == 0:
        return 0
    try:
        la.inv(matrix)
    except la.LinAlgError:
        return -1
    augmented_matrix = np.append(matrix, vector, axis=1)
    matrix_size = len(augmented_matrix)
    for i in range(0, matrix_size):
        for j in range(i, matrix_size):
            if i == j:
                column = [row[i] for row in augmented_matrix]
                column_size = len(column)
                if augmented_matrix[i][i] == 0:
                    for k in range(i, column_size):
                        if column[k] != 0:
                            aux = augmented_matrix[k]
                            augmented_matrix[k] = augmented_matrix[i]
                            augmented_matrix[i] = aux
                            break

                if augmented_matrix[i][i] == 0:
                    return 1

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
    vector = []
    for _ in range(matrix_size):
        vector.append(0)
    vector[matrix_size - 1] = step_matrix[matrix_size - 1][matrix_size] / \
        step_matrix[matrix_size - 1][matrix_size - 1]
    i = matrix_size - 2
    while i >= 0:
        result = 0
        data_size = len(vector) - 1
        while data_size >= 0:
            result += (step_matrix[i][data_size] * vector[data_size])
            data_size -= 1
        vector[i] = (step_matrix[i][matrix_size] - result) / step_matrix[i][i]
        i -= 1
    return vector


class Gauss(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = np.array(body_params["matrix"])
        vector = np.array(body_params["vector"])
        x_values = get_values(stepped_matrix(matrix, vector), len(matrix))
        pivoted_matrix = stepped_matrix(matrix, vector).tolist()
        json_values = json.loads(json.dumps({"PivotedMatrix": pivoted_matrix, "ValuesX": x_values}))
        return json_values
