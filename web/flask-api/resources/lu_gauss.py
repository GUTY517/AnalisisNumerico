#! /usr/bin/env python3

'''Lower and upper matrix Gauss method using scipy'''

import json
import numpy as np
from scipy.linalg import lu
from scipy.linalg import lu_factor, lu_solve
from flask_restful import Resource
from flask import request


def lu_gauss(matrix, vector):
    '''Lower and upper matrix Gauss method'''
    augmented_matrix = np.append(matrix, vector, axis=1)
    permuted_matrix, lower_triangular_matrix, upper_triangular_matrix = lu(
        matrix)
    lower_upper_matrix, pivoted_indices = lu_factor(matrix)
    return augmented_matrix, permuted_matrix, lower_triangular_matrix, upper_triangular_matrix, lu_solve((lower_upper_matrix, pivoted_indices), vector)


class LuGauss(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]
        augmented_matrix, permuted_matrix, lower_triangular_matrix, upper_triangular_matrix, answer = lu_gauss(
            matrix, vector)
        json_response = json.loads(json.dumps(
                                             {
                                                "augmented_matrix":augmented_matrix.tolist(),
                                                "permuted_matrix":permuted_matrix.tolist(),
                                                "L":lower_triangular_matrix.tolist(),
                                                "U":upper_triangular_matrix.tolist(),
                                                "solution":answer.tolist()
                                            }))

        return json_response