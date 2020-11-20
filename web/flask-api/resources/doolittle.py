#! /usr/bin/env python3
'''Doolittle method implemented in numpy'''

import json
import numpy as np
from scipy.linalg import solve
from flask_restful import Resource
from flask import request

def doolittle(matrix):
    '''Doolittle implementation using numpy'''
    matrix_size = matrix.shape[0]
    upper_triangular_matrix = np.zeros((matrix_size, matrix_size), dtype=np.double)
    lower_triangular_matrix = np.eye(matrix_size, dtype=np.double)

    for k in range(matrix_size):
        upper_triangular_matrix[k, k:] = matrix[k, k:] - \
            lower_triangular_matrix[k, :k] @ upper_triangular_matrix[:k, k:]
        lower_triangular_matrix[(k+1):, k] = (matrix[(k+1):, k] - lower_triangular_matrix[(
            k+1):, :] @ upper_triangular_matrix[:, k]) / upper_triangular_matrix[k, k]
    return lower_triangular_matrix, upper_triangular_matrix


class Doolittle(Resource):

    def post(self):
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]
        solved = solve(matrix, vector)

        lower_triangular_matrix, upper_triangular_matrix = doolittle(matrix)
        table_lower_triangular_matrix = json.dumps(lower_triangular_matrix.tolist())
        lower_json_table = json.loads(table_lower_triangular_matrix)
        table_upper_triangular_matrix = json.dumps(upper_triangular_matrix)
        upper_triangular_matrix = json.loads(table_upper_triangular_matrix)
        return lower_json_table, upper_triangular_matrix
