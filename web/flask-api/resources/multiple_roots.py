from __future__ import print_function
import math
import json
import sympy
from decimal import Decimal
from flask_restful import Resource
from flask import request
import pandas as pd
from resources.f_function import f_x as fx
from flask import abort

def multiple_roots(function, x_0, tolerance, iterations):
    '''Multiple roots method'''
    table = pd.DataFrame(columns=['Iteration', 'xi', 'f(xi)',
                                  'Error'])
    function = fx(function=function, g_function='')
    f_x = function.get_f_components(x_0)[0]
    deriv_f = function.get_f_components(x_0)[2]
    deriv_f2 = function.get_f_components(x_0)[3]
    iteration = 0
    error = tolerance + 1
    table = table.append(pd.Series([iteration, x_0, '%.2E' % Decimal(str(f_x)), '-'], index=table.columns), ignore_index=True)
    while error > tolerance and f_x != 0 and deriv_f != 0 and iteration < iterations:
        numerator = f_x * deriv_f
        denominator = (deriv_f**2) - (f_x * deriv_f2)
        x_1 = x_0 - (numerator / denominator)
        f_x = function.get_f_components(x_1)[0]
        deriv_f = function.get_f_components(x_1)[2]
        deriv_f2 = function.get_f_components(x_1)[3]
        error = abs((x_1-x_0))
        x_0 = x_1
        iteration += 1
        table = table.append(pd.Series([iteration, x_1, '%.2E' % Decimal(str(f_x)), '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
    if f_x == 0:
        root = x_0
    elif error < tolerance:
        root = x_1
    elif deriv_f == 0 and f_x == 0 and deriv_f2 != 0:
        root = x_1
    else:
        root = None
    return root, table


class Multiple_Roots(Resource):

    def post(self):
        body_params = request.get_json()
        function= body_params["function"]
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
            root, table = multiple_roots(function, initial_x0, tolerance, iterations)
            table = table.to_json(orient="records", default_handler=str)
            json_table = json.loads(table)
        except TypeError:
            abort(500, "Function not correctly inputed.")
        return json_table
