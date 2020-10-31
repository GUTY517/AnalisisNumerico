from __future__ import print_function
import math
import json
import sympy
import pandas as pd
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request


def function(num):
    '''Calculates inputed function and it's derivative'''
    sympy.init_printing(use_unicode=True)
    x_sym = sympy.symbols('x')
    f_x = sympy.log((sympy.sin(x_sym)*sympy.sin(x_sym)) + 1) - 1/2
    f_n = f_x.evalf(subs={x_sym: num})
    deriv_f = sympy.Derivative(f_x, x_sym).doit()
    derivative = deriv_f.evalf(subs={x_sym: num})
    return (f_n, derivative)


def newton(x_0, tolerance, iterations):
    '''Newton method implemetation'''
    table = pd.DataFrame(columns=['Iteration', 'xi', 'f(xi)', 'Error'])
    f_x = function(x_0)[0]
    deriv_f = function(x_0)[1]
    iteration = 0
    error = tolerance + 1
    table = table.append(pd.Series([iteration, x_0, '%.2E' % f_x, '-'], index=table.columns), ignore_index=True)
    while error > tolerance and f_x != 0 and deriv_f != 0 and iteration < iterations:
        x_1 = x_0 - (f_x/deriv_f)
        f_x = function(x_1)[0]
        deriv_f = function(x_1)[1]
        error = abs((x_1-x_0)/x_1)
        x_0 = x_1
        iteration += 1
        table = table.append(pd.Series([iteration, x_1, '%.2E' %
                       f_x, '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
    if f_x == 0:
        root = x_0
    elif error < tolerance:
        root = x_1
    elif deriv_f == 0:
        root = (x_1, "Multiple root found")
    else:
        root = None
    return root, table


class Newton(Resource):
    def post(self):
        body_params = request.get_json()
        initial_x0 = body_params["initial_x0"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100
        root, table = newton(initial_x0, tolerance, iterations)
        table = table.to_json(orient="records", default_handler=str)
        json_table = json.loads(table)
        return json_table
