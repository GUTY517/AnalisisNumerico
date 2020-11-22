from __future__ import print_function
import math
import json
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request
from resources.f_function import f_x
from flask import abort


def bisection(function, initial_b, initial_a, tolerance, iterations):
    '''Main function to calculate the root of the provided function'''
    # Output table titles
    raw_function = f_x(function=function, g_function='')
    table = PrettyTable(['Iteration', 'a', 'xm', 'b', 'f(xm)', 'Error'])
    fbi = raw_function.get_f_components(initial_b)[0]
    fai = raw_function.get_f_components(initial_a)[0]
    root = 0
    if fbi == 0:
        root = initial_b
    elif fai == 0:
        root = initial_a
    elif fbi * fai < 0:
        x_m = (initial_b + initial_a)/2
        fxm = raw_function.get_f_components(x_m)[0]
        iteration = 1
        error = tolerance + 1
        table.add_row([iteration, initial_b, x_m,
                       initial_a, '%.2E' % fxm, '-'])
        while error > tolerance and fxm != 0 and iteration < iterations:
            if fbi * fxm < 0:
                initial_a = x_m
                fai = fxm
            else:
                initial_b = x_m
                fbi = fxm
            aux = x_m
            x_m = (initial_b + initial_a)/2
            fxm = raw_function.get_f_components(x_m)[0]
            error = abs(x_m-aux)
            iteration += 1
            table.add_row([iteration, initial_b, x_m, initial_a, '%.2E' % fxm, '%.2E' %
                           Decimal(str(error))])
        if fxm == 0:
            root = x_m
        elif error < tolerance:
            root = x_m
        else:
            root = None
    else:
        root = None
    return root, json.loads(table.get_json_string())


class Bisection(Resource):

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
            root, json_table = bisection(function, initial_b, initial_a, tolerance, iterations)
        except TypeError:
            abort(500, "Funtion not correctly inputed.")
        if(root == None):
            abort(500, "Root not found!")
        return json_table
