#! /usr/bin/env python3
'''Get root number using fixed point method'''

from __future__ import print_function
import math
from decimal import Decimal
from prettytable import PrettyTable

def function(num):
    '''Calculates inputed function'''
    f_x = (math.exp(num)) - math.sin(4*num)
    return f_x

def function_g(num):
    '''Calculates second inputed function'''
    f_x = (math.exp(num+1)-(7*(num**2))+2)/4
    return f_x

def fixed_point(x_a, tolerance, iterations):
    '''Main function of the fixed point'''
    table = PrettyTable(['Iteration', 'x_n', 'f(x_n)', 'Error'])
    f_x = function(x_a)
    iteration = 0
    error = tolerance + 1
    table.add_row([iteration, x_a, f_x, '-'])
    while f_x != 0 and error > tolerance and iteration < iterations:
        x_n = function_g(x_a)
        f_x = function(x_n)
        error = abs((x_n-x_a))
        x_a = x_n
        iteration += 1
        table.add_row([iteration, x_n, f_x, '%.2E' % Decimal(str(error))])
    if f_x == 0:
        root = x_a
    elif error < tolerance:
        root = (x_a, '%.2E' % Decimal(str(error)))
    else:
        root = (None, iterations)
    print(table)
    return root

print(fixed_point(3.5, 1e-07, 100))
