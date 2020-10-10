#! /usr/bin/env python3
'''Script to calculate multiple roots using secant method'''

from __future__ import print_function
import math
from decimal import Decimal
from prettytable import PrettyTable


def function(num):
    '''Calculate inputed function'''
    f_x = math.exp(num+1)-(7*(num**2))-(4*num)+2 + \
        (7*(math.sin((num**2)-8)*math.sin((num**2)-8)))
    return f_x


def secant(x_0, x_1, tolerance, iterations):
    '''Secant method to calculate multiple roots'''
    table = PrettyTable(['Iteration', 'Xn', 'f(Xm)', 'Error'])
    f_x0 = function(x_0)
    root = 0
    if f_x0 == 0:
        root = x_0
    else:
        f_x1 = function(x_1)
        iteration = 0
        error = tolerance + 1
        den = f_x1 - f_x0
        table.add_row([iteration, x_0, '%.2E' % Decimal(str(f_x0)), '-'])
        iteration += 1
        table.add_row([iteration, x_1, '%.2E' % Decimal(str(f_x1)), '-'])
        while error > tolerance and f_x1 != 0 and den != 0 and iteration < iterations:
            iteration += 1
            x_2 = x_1 - ((f_x1 * (x_1 - x_0)) / den)
            error = abs((x_2-x_1))
            x_0 = x_1
            f_x0 = f_x1
            x_1 = x_2
            f_x1 = function(x_1)
            den = f_x1 - f_x0
            table.add_row([iteration, x_1, '%.2E' % Decimal(
                str(f_x1)), '%.2E' % Decimal(str(error))])
        if f_x1 == 0:
            root = x_1
        elif error < tolerance:
            root = (x_1, '%.2E' % Decimal(str(error)))
        elif den == 0:
            root = (x_1, "Multiple root found")
        else:
            root = None
    print(table)
    return root


print(secant(3.1, 3.7, 1E-07, 100))
