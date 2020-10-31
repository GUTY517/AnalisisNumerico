from __future__ import print_function
import math
import json
import sympy
from decimal import Decimal
from flask_restful import Resource
from flask import request
import pandas as pd


def function(number):
    '''Calculate the inputed function'''
    sympy.init_printing(use_unicode=True)
    x_sym = sympy.symbols('x')
    f_x = sympy.exp(x_sym) - x_sym - 1
    f_n = f_x.evalf(subs={x_sym: number})
    deriv_f = sympy.Derivative(f_x, x_sym).doit()
    derivative = deriv_f.evalf(subs={x_sym: number})
    deriv_f2 = sympy.Derivative(deriv_f, x_sym).doit()
    derivative2 = deriv_f2.evalf(subs={x_sym: number})
    return (f_n, derivative, derivative2)


def multiple_roots(x_0, tolerance, iterations):
    '''Multiple roots method'''
    table = pd.DataFrame(columns=['Iteration', 'xi', 'f(xi)',
                         'Error'])
    f_x = function(x_0)[0]
    deriv_f = function(x_0)[1]
    deriv_f2 = function(x_0)[2]
    iteration = 0
    error = tolerance + 1
    table = table.append(pd.Series([iteration, x_0, '%.2E' % Decimal(str(f_x)), '-'], index=table.columns), ignore_index=True )
    while error > tolerance and f_x != 0 and deriv_f != 0 and iteration < iterations:
        numerator = f_x * deriv_f
        denominator = (deriv_f**2) - (f_x * deriv_f2)
        x_1 = x_0 - (numerator / denominator)
        f_x = function(x_1)[0]
        deriv_f = function(x_1)[1]
        deriv_f2 = function(x_1)[2]
        error = abs((x_1-x_0))
        x_0 = x_1
        iteration += 1
        table = table.append(pd.Series([iteration, x_1, '%.2E' % Decimal(
            str(f_x)), '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
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
        initial_x0 = body_params["initial_x0"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100

        root, table = multiple_roots(initial_x0, tolerance, iterations)
        table = table.to_json(orient="records", default_handler=str)
        json_table = json.loads(table)
        return json_table
