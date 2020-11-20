#! /usr/bin/env python3
'''Cholesky method using numpy'''

import warnings
import json
import numpy as np
from scipy.linalg import solve
from flask_restful import Resource
from flask import request


def cholesky(matrix_a):
    '''Cholesky method'''
    warnings.filterwarnings('error')
    matrix_size = matrix_a.shape[0]
    lower_triangular_matrix = np.zeros(
        (matrix_size, matrix_size), dtype=np.double)
    upper_triangular_matrix = np.zeros(
        (matrix_size, matrix_size), dtype=np.double)

    for k in range(matrix_size):
        try:
            lower_triangular_matrix[k, k] = np.sqrt(
                matrix_a[k, k] - np.sum(lower_triangular_matrix[k, :] ** 2))
            upper_triangular_matrix[k, k:] = (
                matrix_a[k, k:] - lower_triangular_matrix[k, :k]
                @ upper_triangular_matrix[:k, k:]) / lower_triangular_matrix[k, k]
            lower_triangular_matrix[(k+1):, k] = (matrix_a[(k+1):, k] - lower_triangular_matrix[(
                k+1):, :] @ lower_triangular_matrix[:, k]) / lower_triangular_matrix[k, k]
        except Warning:
            return "Matrix contains complex numbers"

    return lower_triangular_matrix, upper_triangular_matrix


class Cholesky(Resource):

    def post(self):
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]
        solved = solve(matrix, vector)
        lower_triangular_matrix, upper_triangular_matrix = cholesky(matrix)
        table_lower_triangular_matrix = json.dumps(lower_triangular_matrix.tolist())
        lower_json_table = json.loads(table_lower_triangular_matrix)
        table_upper_triangular_matrix = json.dumps(upper_triangular_matrix.tolist())
        upper_json_table = json.loads(table_upper_triangular_matrix)
        return lower_json_table, upper_json_table
