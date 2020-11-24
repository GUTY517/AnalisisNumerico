from __future__ import print_function
import math
import json
import sympy
import pandas as pd
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request
from resources.f_function import f_x as fx
from flask import abort


def newton(function, x_0, tolerance, iterations):
    '''Newton method implemetation'''
    table = pd.DataFrame(columns=['Iteration', 'xi', 'f(xi)', 'Error'])
    function = fx(function=function, g_function='')
    f_x = function.get_f_components(x_0)[0]
    deriv_f = function.get_f_components(x_0)[2]
    iteration = 0
    error = tolerance + 1
    table = table.append(pd.Series([iteration, x_0, '%.2E' % f_x, '-'], index=table.columns), ignore_index=True)
    while error > tolerance and f_x != 0 and deriv_f != 0 and iteration < iterations:
        x_1 = x_0 - (f_x/deriv_f)
        f_x = function.get_f_components(x_1)[0]
        deriv_f = function.get_f_components(x_1)[2]
        error = abs((x_1-x_0)/x_1)
        x_0 = x_1
        iteration += 1
        table = table.append(pd.Series([iteration, x_1, '%.2E' %f_x, '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
    if f_x == 0:
        root = x_0
    elif error < tolerance:
        root = x_1
    elif deriv_f == 0:
        try:
            root = (x_1, "Multiple root found")
        except UnboundLocalError:
            abort(500, "Inputed x0 value is not correct")
    else:
        root = None
    return root, table


class Newton(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        function = body_params["function"]
        initial_x0 = body_params["initial_x0"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100
        if iterations < 0:
            abort(500, "Inadequate iterations.")
        if tolerance < 0:
            abort(500, "Inadequate tolerance.")
        try:
            root, table = newton(function, initial_x0, tolerance, iterations)
            table = json.loads(table.to_json(orient="records", default_handler=str))
            json_data = json.loads(json.dumps({"Root": [float(root)], "Table": table}))
            if root is None:
                abort(500, "Root not found!")
        except TypeError:
            abort(500, "Function not correctly inputed.")
        return json_data
