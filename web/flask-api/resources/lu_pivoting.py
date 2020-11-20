#! /usr/bin/env python3
'''LU Pivoting method implementation using scipy'''

import json
from scipy.linalg import lu
from scipy.linalg import solve
from flask_restful import Resource
from flask import request


def lu_pivoting(matrix, vector):
    '''LU pivoting method'''

    augmented_matrix = np.append(matrix, vector, axis=1)

    permuted_matrix, lower_triangular_matrix, upper_triangular_matrix = lu(
        matrix)
    return augmented_matrix, permuted_matrix, lower_triangular_matrix, upper_triangular_matrix, solve(matrix, vector)


class LuGauss(Resource):

    def post(self):
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]
        augmented_matrix, permuted_matrix, lower_triangular_matrix, upper_triangular_matrix, answer = lu_pivoting(matrix, vector)
        table_augmented_matrix = json.dumps(augmented_matrix.tolist())
        augmented_matrix_table = json.loads(table_augmented_matrix)
        table_permuted_matrix = json.dumps(permuted_matrix.tolist())
        permuted_matrix_table = json.loads(table_permuted_matrix)
        table_lower_triangular_matrix = json.dumps(lower_triangular_matrix.tolist())
        lower_json_table = json.loads(table_lower_triangular_matrix)
        table_upper_triangular_matrix = json.dumps(upper_triangular_matrix.tolist())
        upper_json_table = json.loads(table_upper_triangular_matrix)
        return augmented_matrix_table, permuted_matrix_table, lower_json_table, upper_json_table, answer