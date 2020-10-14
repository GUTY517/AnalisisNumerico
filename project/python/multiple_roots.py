#! /usr/bin/env python3
'''Script to calculate multiple roots using the multiple roots method'''

from __future__ import print_function
from decimal import Decimal
import sympy
from prettytable import PrettyTable


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
    table = PrettyTable(['Iteration', 'xi', 'f(xi)',
                         'Error'])
    f_x = function(x_0)[0]
    deriv_f = function(x_0)[1]
    deriv_f2 = function(x_0)[2]
    iteration = 0
    error = tolerance + 1
    table.add_row([iteration, x_0, '%.2E' % Decimal(str(f_x)), '-'])
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
        table.add_row([iteration, x_1, '%.2E' % Decimal(str(f_x)), '%.2E' % Decimal(str(error))])
    if f_x == 0:
        root = x_0
    elif error < tolerance:
        root = x_1
    elif deriv_f == 0 and f_x == 0 and deriv_f2 != 0:
        root = x_1
    else:
        root = None
    print(table)
    return root


print("There is an aproximate root in:", multiple_roots(1, 1e-07, 100))
