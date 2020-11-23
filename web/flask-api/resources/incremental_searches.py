#! /usr/bin/env python3
'''Incremental method to find roots of a function'''

from __future__ import print_function
import json
from flask_restful import Resource
from flask import request
from resources.f_function import f_x
from flask import abort


def verify_complex(error):
    '''Check for complex numbers in results'''
    if 'I' in error:
        abort(500, "Cannot execute method since answer has complex numbers")
    return 0


def incremental_search(function, x_0, delta, iterations):
    '''Incremental search method'''
    raw_function = f_x(function=function, g_function='')
    fx_1 = raw_function.get_f_components(x_0)[0]
    root = 0
    roots = []
    if fx_1 == 0:
        root = x_0
        roots.append(x_0)
    else:
        x_1 = x_0 + delta
        iteration = 1
        fx1 = raw_function.get_f_components(x_1)[0]
        while iteration < iterations:
            if fx1 == 0:
                root = x_1
                roots.append(x_1)
            elif verify_complex(str(fx_1 * fx1)) > 0:
                abort(500, "Answer has complex numbers")
            elif fx_1 * fx1 < 0:
                root = (x_0, x_1)
                roots.append(root)
            else:
                root = None
            x_0 = x_1
            fx_1 = fx1
            x_1 = x_0 + delta
            fx1 = raw_function.get_f_components(x_1)[0]
            iteration += 1
    return roots


class IncrementalSearch(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        function = body_params["function"]
        x_0 = body_params["x0"]
        delta_x = body_params["delta_x"]
        iterations = body_params["iterations"]
        if not iterations:
            iterations = 100
        if iterations <= 0:
            abort(500, "Inadequate iterations.")
        json_data = json.loads(json.dumps({"Roots": incremental_search(function, x_0, delta_x, iterations)}))
        return json_data
