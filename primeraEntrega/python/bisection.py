#! /usr/bin/env python3
'''Script to calculate the root of a function using bisection method'''

from __future__ import print_function
import math
from decimal import Decimal
from prettytable import PrettyTable


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
        table.add_row([iteration, initial_b, x_m, initial_a, '%.2E' % fxm, '-'])
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
        print(table)
    else:
        root = "Root not found!"
    return root


print("There is an aproximate root in:", bisection(0, 1, 1e-07, 100))
