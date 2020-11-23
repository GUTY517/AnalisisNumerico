#! /usr/bin/env python3
'''Crout implementation using numpy and scipy'''

import json
import numpy as np
from scipy.linalg import solve, LinAlgError
from flask_restful import Resource
from flask import request
from flask import abort


def crout(matrix):
    '''Crout method'''
    matrix_size = matrix.shape[0]
    upper_triangular_matrix = np.zeros(
        (matrix_size, matrix_size), dtype=np.double)
    lower_triangular_matrix = np.zeros(
        (matrix_size, matrix_size), dtype=np.double)

    for k in range(matrix_size):
        lower_triangular_matrix[k, k] = matrix[k, k] - \
            lower_triangular_matrix[k, :] @ upper_triangular_matrix[:, k]
        upper_triangular_matrix[k, k:] = (
            matrix[k, k:] - lower_triangular_matrix[k, :k]
            @ upper_triangular_matrix[:k, k:]) / lower_triangular_matrix[k, k]
        lower_triangular_matrix[(k+1):, k] = (matrix[(k+1):, k] - lower_triangular_matrix[(
            k+1):, :] @ upper_triangular_matrix[:, k]) / upper_triangular_matrix[k, k]

    return lower_triangular_matrix, upper_triangular_matrix


class Crout(Resource):
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
        lower_triangular_matrix, upper_triangular_matrix = crout(matrix)
        lower_triangular_matrix = lower_triangular_matrix.tolist()
        upper_triangular_matrix = upper_triangular_matrix.tolist()
        solution = solved.tolist()
        json_response = json.loads(json.dumps({"LowerMatrix":lower_triangular_matrix, "UpperMatrix":upper_triangular_matrix, "Answer":solution}))
        return json_response
