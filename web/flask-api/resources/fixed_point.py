from __future__ import print_function
import math
import json
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request
from resources.f_function import f_x as fx
import pandas as pd


def function(num):
    '''Calculates inputed function'''
    f_x = (math.log((math.sin(num)*math.sin(num)) + 1)) - (1/2) - num
    return f_x


def function_g(num):
    '''Calculates second inputed function'''
    f_x = (math.log((math.sin(num)*math.sin(num)) + 1)) - (1/2)
    return f_x


def fixed_point(function, g_function, x_a, tolerance, iterations):
    '''Main function of the fixed point'''
    table = pd.DataFrame(columns=['Iteration', 'xi', 'g(xi)', 'f(xi)', 'Error'])
    func = fx(function=function, g_function=g_function)
    # print(table)
    f_x = func.get_f_components(x_a)[0]
    g_x = func.get_g_components(x_a)[0]
    iteration = 0
    error = tolerance + 1
    table = table.append(pd.Series([iteration, x_a, g_x, '%.2E' % f_x, '-'], index=table.columns), ignore_index=True)
    print(table)
    while f_x != 0 and error > tolerance and iteration < iterations:
        x_i = func.get_g_components(x_a)[0]
        f_x = func.get_g_components(x_i)[0]
        error = abs((x_i-x_a))
        x_a = x_i
        iteration += 1
        table = table.append(pd.Series([iteration, x_i, g_x, '%.2E' %
                       f_x, '%.2E' % Decimal(str(error))], index=table.columns), ignore_index=True)
    if f_x == 0:
        root = x_a
    elif error < tolerance:
        root = x_a
    else:
        root = None
        print("Root not found!")
    # print(table)
    return root, table


class Fixed_Point(Resource):

    def post(self):
        body_params = request.get_json()
        funct = body_params["function"]
        g_function = body_params["g_function"]
        initial_ax = body_params["initial_ax"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100
        print(funct)
        print(g_function)
        root, table = fixed_point(funct, g_function, initial_ax, tolerance, iterations)
        table = table.to_json(orient="records", default_handler=str)
        json_table = json.loads(table)
        return json_table

# print("There is an aproximate root in:", fixed_point(0.5, 1e-07, 100))
