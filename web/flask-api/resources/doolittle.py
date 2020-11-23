#! /usr/bin/env python3
'''Doolittle method implemented in numpy'''

import json
import numpy as np
from scipy.linalg import solve, LinAlgError
from flask_restful import Resource
from flask import request
from flask import abort


def doolittle(matrix):
    '''Doolittle implementation using numpy'''
    matrix_size = matrix.shape[0]
    upper_triangular_matrix = np.zeros(
        (matrix_size, matrix_size), dtype=np.double)
    lower_triangular_matrix = np.eye(matrix_size, dtype=np.double)

    for k in range(matrix_size):
        upper_triangular_matrix[k, k:] = matrix[k, k:] - \
            lower_triangular_matrix[k, :k] @ upper_triangular_matrix[:k, k:]
        lower_triangular_matrix[(k+1):, k] = (matrix[(k+1):, k] - lower_triangular_matrix[(
            k+1):, :] @ upper_triangular_matrix[:, k]) / upper_triangular_matrix[k, k]
    return lower_triangular_matrix, upper_triangular_matrix


class Doolittle(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = np.array(body_params["matrix"])
        vector = np.array(body_params["vector"])
        try:
            solved = solve(matrix, vector)
        except LinAlgError:
            abort(500, "Imposible to perform this action because matrix is singular")
        lower_triangular_matrix, upper_triangular_matrix = doolittle(matrix)
        lower_triangular_matrix = lower_triangular_matrix.tolist()
        upper_triangular_matrix = upper_triangular_matrix.tolist()
        solution = solved.tolist()
        json_response = json.loads(json.dumps({"L":lower_triangular_matrix, "U":upper_triangular_matrix, "solution":solution}))
        return json_response
