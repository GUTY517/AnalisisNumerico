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
    '''Calculate inputed function'''
    f_x = (math.log((math.sin(num)*math.sin(num)) + 1)) - (1/2)
    return f_x


def secant(x_0, x_1, tolerance, iterations):
    '''Secant method to calculate multiple roots'''
    table = PrettyTable(['Iteration', 'xi', 'f(xi)', 'Error'])
    f_x0 = function(x_0)
    root = 0
    if f_x0 == 0:
        root = x_0
    else:
        f_x1 = function(x_1)
        iteration = 0
        error = tolerance + 1
        denominator = f_x1 - f_x0
        table.add_row([iteration, x_0, '%.2E' % Decimal(str(f_x0)), '-'])
        iteration += 1
        table.add_row([iteration, x_1, '%.2E' % Decimal(str(f_x1)), '-'])
        while error > tolerance and f_x1 != 0 and denominator != 0 and iteration < iterations:
            iteration += 1
            x_2 = x_1 - ((f_x1 * (x_1 - x_0)) / denominator)
            error = abs((x_2-x_1))
            x_0 = x_1
            f_x0 = f_x1
            x_1 = x_2
            f_x1 = function(x_1)
            denominator = f_x1 - f_x0
            table.add_row([iteration, x_1, '%.2E' % Decimal(
                str(f_x1)), '%.2E' % Decimal(str(error))])
        if f_x1 == 0:
            root = x_1
        elif error < tolerance:
            root = x_1
        elif denominator == 0:
            root = (x_1, "Multiple root found")
        else:
            root = None
    # print(table)
    return root, json.loads(table.get_json_string())


class Secant(Resource):

    def post(self):
        body_params = request.get_json()
        initial_x0 = body_params["initial_x0"]
        initial_x1 = body_params["initial_x1"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100

        root, table = secant(initial_x0, initial_x1, tolerance, iterations)
        return table
        