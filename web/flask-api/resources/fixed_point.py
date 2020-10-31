from __future__ import print_function
import math
import json
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request


def function(num):
    '''Calculates inputed function'''
    f_x = (math.log((math.sin(num)*math.sin(num)) + 1)) - (1/2) - num
    return f_x


def function_g(num):
    '''Calculates second inputed function'''
    f_x = (math.log((math.sin(num)*math.sin(num)) + 1)) - (1/2)
    return f_x


def fixed_point(x_a, tolerance, iterations):
    '''Main function of the fixed point'''
    table = PrettyTable(['Iteration', 'xi', 'g(xi)', 'f(xi)', 'Error'])
    f_x = function(x_a)
    g_x = function_g(x_a)
    iteration = 0
    error = tolerance + 1
    table.add_row([iteration, x_a, g_x, '%.2E' % f_x, '-'])
    while f_x != 0 and error > tolerance and iteration < iterations:
        x_i = function_g(x_a)
        f_x = function(x_i)
        error = abs((x_i-x_a))
        x_a = x_i
        iteration += 1
        table.add_row([iteration, x_i, g_x, '%.2E' %
                       f_x, '%.2E' % Decimal(str(error))])
    if f_x == 0:
        root = x_a
    elif error < tolerance:
        root = x_a
    else:
        root = None
        print("Root not found!")
    return root, json.loads(table.get_json_string())


class Fixed_Point(Resource):

    def post(self):
        body_params = request.get_json()
        initial_ax = body_params["initial_ax"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100

        root, json_table = fixed_point(initial_ax, tolerance, iterations)
        return json_table

# print("There is an aproximate root in:", fixed_point(0.5, 1e-07, 100))
