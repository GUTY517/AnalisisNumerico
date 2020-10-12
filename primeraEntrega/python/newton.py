#! /usr/bin/env python3
'''Script to calculate multiple roots using Newton method'''

from __future__ import print_function
from decimal import Decimal
import sympy
from prettytable import PrettyTable

def function(num):
    '''Calculates inputed function and it's derivative'''
    sympy.init_printing(use_unicode=True)
    x_sym = sympy.symbols('x')
    f_x = sympy.log((sympy.sin(x_sym)*sympy.sin(x_sym)) + 1) - 1/2
    f_n = f_x.evalf(subs={x_sym:num})
    deriv_f = sympy.Derivative(f_x, x_sym).doit()
    derivative = deriv_f.evalf(subs={x_sym:num})
    return (f_n, derivative)

def newton(x_0, tolerance, iterations):
    '''Newton method implemetation'''
    table = PrettyTable(['Iteration', 'xi', 'f(xi)', 'Error'])
    f_x = function(x_0)[0]
    deriv_f = function(x_0)[1]
    iteration = 0
    error = tolerance + 1
    table.add_row([iteration, x_0, '%.2E' % f_x, '-'])
    while error > tolerance and f_x != 0 and deriv_f != 0 and iteration < iterations:
        x_1 = x_0 - (f_x/deriv_f)
        f_x = function(x_1)[0]
        deriv_f = function(x_1)[1]
        error = abs((x_1-x_0)/x_1)
        x_0 = x_1
        iteration += 1
        table.add_row([iteration, x_1, '%.2E' % f_x, '%.2E' % Decimal(str(error))])
    if f_x == 0:
        root = x_0
    elif error < tolerance:
        root = x_1
    elif deriv_f == 0:
        root = (x_1, "Multiple root found")
    else:
        root = None
    print(table)
    return root

print("There is an aproximate root in:", newton(0.5, 1e-07, 100))
