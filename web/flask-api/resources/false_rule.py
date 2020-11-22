from __future__ import print_function
import math
import json
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from resources.f_function import f_x
from flask import request
from flask import abort
import pandas as pd


def false_rule(function, initial_b, initial_a, tolerance, iterations):
    '''Returns root of a function using false rule method'''
    raw_function = f_x(function=function, g_function='')
    table = pd.DataFrame(columns=['Iteration', 'a', 'xm', 'b', 'f(xm)', 'Error'])
    fxi = raw_function.get_f_components(initial_b)[0]
    fxs = raw_function.get_f_components(initial_a)[0]
    s_i = initial_b - initial_a
    helper = fxi - fxs
    root = 0
    if fxi == 0:
        root = initial_b
    elif fxs == 0:
        root = initial_a
    elif fxi * fxs < 0:
        if helper != 0:
            x_m = initial_b - ((fxi*s_i)/helper)
            fxm = raw_function.get_f_components(x_m)[0]
            interation = 1
            error = tolerance + 1
            table = table.append(pd.Series([interation, initial_b, x_m, initial_a, '%.2E' % fxm, '-'], index=table.columns), ignore_index=True)
            while error > tolerance and fxm != 0 and interation < iterations:
                if fxi * fxm < 0:
                    initial_a = x_m
                    fxs = fxm
                else:
                    initial_b = x_m
                    fxi = fxm
                aux = x_m
                s_i = initial_b - initial_a
                helper = fxi - fxs
                if helper == 0:
                    break
                x_m = initial_b - ((fxi*s_i)/helper)
                fxm = raw_function.get_f_components(x_m)[0]
                error = abs(x_m-aux)
                interation += 1
                table = table.append(pd.Series([interation, initial_b, x_m, initial_a, '%.2E' % fxm, '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
            if fxm == 0:
                root = x_m
            elif error < tolerance:
                root = x_m
            else:
                root = None
        else:
            root = False
    else:
        root = None
    return root, table


class False_Rule(Resource):

    def post(self):
        body_params = request.get_json()
        function = body_params["function"]
        initial_a = body_params["initial_a"]
        initial_b = body_params["initial_b"]
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
            root, table = false_rule(function, initial_b, initial_a, tolerance, iterations)
            json_table = json.loads(table.to_json(orient="records", default_handler=str))
        except TypeError:
            abort(500, "Function not correctly inputed.")
        if root == None:
            abort(500, "Root not found!")
        return json_table
