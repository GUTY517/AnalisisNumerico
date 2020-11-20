#! /usr/bin/env python3

from numpy import linalg as la
import numpy as np
from flask_restful import Resource
from flask import request


def stepped_matrix(A, b):
    if la.det(A) == 0:
        return 0
    try:
        la.inv(A)
    except la.LinAlgError:
        return -1
    augmented_matrix = np.append(A, b, axis=1)
    matrix_size = len(augmented_matrix)
    for i in range(0, matrix_size):
        for j in range(i, matrix_size):
            if i == j:
                column = [row[i] for row in augmented_matrix]
                lenColumn = len(column)
                if augmented_matrix[i][i] == 0:
                    for k in range(i, lenColumn):
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
                for k in range(0, len(row2)):
                    row2[k] -= (mult * row1[k])
                augmented_matrix[j] = row2
    return augmented_matrix


def get_values(step_matrix, matrix_size):
    vector = []
    for x in range(matrix_size):
        vector.append(0)
    vector[matrix_size - 1] = step_matrix[matrix_size - 1][matrix_size] / \
        step_matrix[matrix_size - 1][matrix_size - 1]
    i = matrix_size - 2
    while i >= 0:
        result = 0
        p = len(vector) - 1
        while p >= 0:
            result += (step_matrix[i][p] * vector[p])
            p -= 1
        vector[i] = (step_matrix[i][matrix_size] - result) / step_matrix[i][i]
        i -= 1
    return vector


def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix


def main(matrix, vector):

    results_x = get_values(stepped_matrix(matrix, vector), len(matrix))
    x_values = '\n'.join([str(elem) for elem in results_x])
    return stepped_matrix(matrix, vector), x_values

class total_pivoting(Resource):

    def post(self):
        body_params = request.get_json()
        matrix = body_params["matrix"]
        vector = body_params["vector"]

        stepped_matrix, x_values = main(matrix, vector)
        table = stepped_matrix.to_json(orient="records", default_handler=str)
        json_table = json.loads(table)
        return json_table
