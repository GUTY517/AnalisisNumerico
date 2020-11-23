#! /usr/bin/env python3
'''Newton Interpolation'''

import json
from flask_restful import Resource
from flask import request


def interpolate_coefficients(x_values, y_values):
    '''Interpolation of coefficients'''
    data_size = len(x_values)

    data = sorted(zip(x_values, y_values), reverse=False)
    x_values, y_values = zip(*data)

    depth = 1
    coefficients = [y_values[0]]
    new_y_values = y_values

    while depth < data_size:
        iterative_data = []

        for i in range(len(new_y_values)-1):
            delta_y = new_y_values[i+1]-new_y_values[i]
            delta_x = x_values[i+depth]-x_values[i]
            iterative_value = (delta_y/delta_x)
            iterative_data.append(iterative_value)
            if i == 0:
                coefficients.append(iterative_value)

        new_y_values = iterative_data
        depth += 1

    return coefficients


def interpolate_values(x_values, y_values):
    '''Interpolate values'''
    data_size = len(x_values)
    data = sorted(zip(x_values, y_values), reverse=False)
    x_values, y_values = zip(*data)

    depth = 1
    coefficients = [y_values[0]]
    new_y_values = y_values

    while depth < data_size:
        iterative_data = []
        for i in range(len(new_y_values)-1):
            delta_y = new_y_values[i+1]-new_y_values[i]
            delta_x = x_values[i+depth]-x_values[i]
            iterative_value = (delta_y/delta_x)
            iterative_data.append(iterative_value)

            if i == 0:
                coefficients.append(iterative_value)

        new_y_values = iterative_data
        depth += 1

    def function(i):
        '''Evaluate interpolated estimate at x'''
        terms = []
        answer = 0
        data_size = len(coefficients)

        for j in range(data_size):
            iterative_value = coefficients[j]
            iterative_x_values = x_values[:j]
            for k in iterative_x_values:
                iterative_value *= (i-k)
            terms.append(iterative_value)
            answer += iterative_value
        return answer
    return function


class NewtonInterpolation(Resource):

    def post(self):
        body_params = request.get_json()
        x_values = body_params["x_values"]
        y_values = body_params["y_values"]
        coefficients = interpolate_coefficients(x_values, y_values)
        json_data = json.loads(json.dumps({"Coefficients":coefficients}))
        return json_data
