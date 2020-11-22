#! /usr/bin/env python3
'''Cholesky method using numpy'''

import warnings
import json
import numpy as np
from scipy.linalg import solve
from flask_restful import Resource
from flask import request
from flask import abort


def cholesky(matrix):
    '''Cholesky method'''
    warnings.filterwarnings('error')
    matrix_size = matrix.shape[0]
    lower_triangular_matrix = np.zeros(
        (matrix_size, matrix_size), dtype=np.double)
    upper_triangular_matrix = np.zeros(
        (matrix_size, matrix_size), dtype=np.double)

    for k in range(matrix_size):
        try:
            lower_triangular_matrix[k, k] = np.sqrt(
                matrix[k, k] - np.sum(lower_triangular_matrix[k, :] ** 2))
            upper_triangular_matrix[k, k:] = (
                matrix[k, k:] - lower_triangular_matrix[k, :k]
                @ upper_triangular_matrix[:k, k:]) / lower_triangular_matrix[k, k]
            lower_triangular_matrix[(k+1):, k] = (matrix[(k+1):, k] - lower_triangular_matrix[(
                k+1):, :] @ lower_triangular_matrix[:, k]) / lower_triangular_matrix[k, k]
        except Warning:
            abort(500, "Matrix can not be computed since it have complex numbers")

    return lower_triangular_matrix, upper_triangular_matrix


class Cholesky(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = np.array(body_params["matrix"])
        vector = np.array(body_params["vector"])
        solved = solve(matrix, vector)
        lower_triangular_matrix, upper_triangular_matrix = cholesky(matrix)
        json_data = json.loads(json.dumps(lower_triangular_matrix.tolist(
        ) + upper_triangular_matrix.tolist() + solved.tolist()))
        return json_data
