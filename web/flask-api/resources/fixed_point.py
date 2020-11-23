from __future__ import print_function
import math
import json
from decimal import Decimal
from flask_restful import Resource
from flask import request
from resources.f_function import f_x as fx
import pandas as pd


def fixed_point(function_f, function_g, x_a, tolerance, iterations):
    '''Main function of the fixed point'''
    table = pd.DataFrame(columns=['Iteration', 'xi', 'g(xi)', 'f(xi)', 'Error'])
    raw_function = fx(function=function_f, g_function=function_g)
    f_x = raw_function.get_f_components(x_a)[0]
    g_x = raw_function.get_g_components(x_a)[0]
    iteration = 0
    error = tolerance + 1
    table = table.append(pd.Series([iteration, x_a, g_x, '%.2E' % f_x, '-'], index=table.columns), ignore_index=True)
    while f_x != 0 and error > tolerance and iteration < iterations:
        x_i = raw_function.get_g_components(x_a)[0]
        f_x = raw_function.get_f_components(x_i)[0]
        error = abs((x_i-x_a))
        x_a = x_i
        iteration += 1
        table = table.append(pd.Series([iteration, x_i, g_x, '%.2E' % f_x, '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
    if f_x == 0:
        root = x_a
    elif error < tolerance:
        root = x_a
    else:
        root = None
        print("Root not found!")
    return root, table


class FixedPoint(Resource):
    '''Flask functions for web page'''

    def post(self):
        '''Web function to get variables from web page, execute method and return answers'''
        body_params = request.get_json()
        function_f = body_params["function_f"]
        function_g = body_params["function_g"]
        initial_ax = body_params["initial_x0"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100
        if iterations <= 0:
            abort(500, "Inadequate iterations.")
        if tolerance <= 0:
            abort(500, "Inadequate tolerance.")
        try:
            root, table = fixed_point(function_f, function_g, initial_ax, tolerance, iterations)
            json_table = json.loads(table.to_json(orient="records", default_handler=str))
            json_data = json.loads(json.dumps({"Root":[float(root)], "Table":json_table}))
        except TypeError:
            abort(500, "Function not correctly inputed.")
        return json_data
