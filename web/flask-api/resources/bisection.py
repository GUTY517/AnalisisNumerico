from __future__ import print_function
import math
import json
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request


def function(num):
    '''Calculates inputed function'''
    f_x = (math.log((math.sin(num)*math.sin(num)) + 1)) - (1/2)
    return f_x


def bisection(initial_b, initial_a, tolerance, iterations):
    '''Main function to calculate the root of the provided function'''
    # Output table titles
    table = PrettyTable(['Iteration', 'a', 'xm', 'b', 'f(xm)', 'Error'])
    fbi = function(initial_b)
    fai = function(initial_a)
    root = 0
    if fbi == 0:
        root = initial_b
    elif fai == 0:
        root = initial_a
    elif fbi * fai < 0:
        x_m = (initial_b + initial_a)/2
        fxm = function(x_m)
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
            fxm = function(x_m)
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
        root = "Root not found!"
    return root, json.loads(table.get_json_string())


class Bisection(Resource):

    def post(self):
        body_params = request.get_json()
        initial_a = body_params["initial_a"]
        initial_b = body_params["initial_b"]
        tolerance = body_params["tolerance"]
        iterations = body_params["iterations"]
        if not tolerance:
            tolerance = 1e-07
        if not iterations:
            iterations = 100
        root, json_table = bisection(initial_b, initial_a, tolerance, iterations)
        # if(root == None):     we need to find some way of handling root errors
        #     abort(500, message="root not found")
        return json_table
