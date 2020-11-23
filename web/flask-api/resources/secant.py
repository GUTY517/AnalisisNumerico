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

def secant(function ,x_0, x_1, tolerance, iterations):
    '''Secant method to calculate multiple roots'''
    table = pd.DataFrame(columns=['Iteration', 'xi', 'f(xi)', 'Error'])
    function = fx(function=function, g_function='')
    f_x0 = function.get_f_components(x_0)[0]
    root = 0
    if f_x0 == 0:
        root = x_0
    else:
        f_x1 = function.get_f_components(x_1)[0]
        iteration = 0
        error = tolerance + 1
        denominator = f_x1 - f_x0
        table = table.append(pd.Series([iteration, x_0, '%.2E' % Decimal(str(f_x0)), '-'], index=table.columns), ignore_index=True)
        iteration += 1
        table = table.append(pd.Series([iteration, x_1, '%.2E' % Decimal(str(f_x1)), '-'], index=table.columns), ignore_index=True)
        while error > tolerance and f_x1 != 0 and denominator != 0 and iteration < iterations:
            iteration += 1
            x_2 = x_1 - ((f_x1 * (x_1 - x_0)) / denominator)
            error = abs((x_2-x_1))
            x_0 = x_1
            f_x0 = f_x1
            x_1 = x_2
            f_x1 = function.get_f_components(x_1)[0]
            denominator = f_x1 - f_x0
            table = table.append(pd.Series([iteration, x_1, '%.2E' % Decimal(
                str(f_x1)), '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
        if f_x1 == 0:
            root = x_1
        elif error < tolerance:
            root = x_1
        elif denominator == 0:
            root = (x_1, "Multiple root found")
        else:
            root = None
    return root, table


class Secant(Resource):

    def post(self):
        body_params = request.get_json()
        function = body_params["function"]
        initial_x0 = body_params["initial_x0"]
        initial_x1 = body_params["initial_x1"]
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
            root, table = secant(function, initial_x0, initial_x1, tolerance, iterations)
            table = json.loads(table.to_json(orient="records", default_handler=str))
            json_data = json.loads(json.dumps({"Root": [float(root)], "Table": table}))
        except TypeError:
            abort(500, "Function not correctly inputed.")
        return json_data
