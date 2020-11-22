#! /usr/bin/env python3
'''LU Pivoting method implementation using scipy'''

import json
import numpy as np
from scipy.linalg import lu
from scipy.linalg import solve
from flask_restful import Resource
from flask import request


def lu_pivoting(matrix, vector):
    '''LU partial pivoting method'''

    augmented_matrix = np.append(matrix, vector, axis=1)
    permuted_matrix, lower_triangular_matrix, upper_triangular_matrix = lu(
        matrix)
    return augmented_matrix, permuted_matrix, lower_triangular_matrix, upper_triangular_matrix, solve(matrix, vector)


class LuPivoting(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]
        augmented_matrix, permuted_matrix, lower_triangular_matrix, upper_triangular_matrix, answer = lu_pivoting(
            matrix, vector)
        json_data = json.loads(json.dumps(augmented_matrix.tolist() + permuted_matrix.tolist(
        ) + lower_triangular_matrix.tolist() + upper_triangular_matrix.tolist() + answer.tolist()))
        return json_data
