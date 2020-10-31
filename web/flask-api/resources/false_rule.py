from __future__ import print_function
import math
import json
from decimal import Decimal
from prettytable import PrettyTable
from flask_restful import Resource
from flask import request


def function(number):
    '''Calculates inputed function'''
    f_x = (math.log((math.sin(number)*math.sin(number)) + 1)) - (1/2)
    return f_x


def false_rule(initial_b, initial_a, tolerance, iterations):
    '''Returns root of a function using false rule method'''
    table = PrettyTable(['Iteration', 'a', 'xm', 'b', 'f(xm)', 'Error'])
    fxi = function(initial_b)
    fxs = function(initial_a)
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
            fxm = function(x_m)
            interation = 1
            error = tolerance + 1
            table.add_row([interation, initial_b, x_m,
                           initial_a, '%.2E' % fxm, '-'])
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
                fxm = function(x_m)
                error = abs(x_m-aux)
                interation += 1
                table.add_row([interation, initial_b, x_m,
                               initial_a, '%.2E' % fxm, '%.2E' % Decimal(str(error))])
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
        ddd = "pene"
    return root, json.loads(table.get_json_string())


class False_Rule(Resource):

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

        return false_rule(initial_b, initial_a, tolerance, iterations)[1]
