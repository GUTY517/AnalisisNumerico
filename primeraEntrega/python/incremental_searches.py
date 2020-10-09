#! /usr/bin/env python3
'''Incremental method to find roots of a function'''

from __future__ import print_function
import math


def verify_complex(error):
    '''Check for complex numbers in results'''
    if 'I' in error:
        return 1
    return 0


def function(num):
    '''Calculates inputed function'''
    f_x = (math.exp(-num) - math.sin(4*num))
    return f_x


def incremental_searches(x_0, delta, iterations):
    '''Incremental search method'''
    f_x = function(x_0)
    root = 0
    roots = [['Roots']]
    if f_x == 0:
        root = x_0
        roots.append(x_0)
    else:
        x_1 = x_0 + delta
        cont = 1
        fx1 = function(x_1)
        while cont < iterations:
            if fx1 == 0:
                root = x_1
                roots.append(x_1)
            elif verify_complex(str(f_x * fx1)) > 0:
                strerr = "Error: obtained results contains complex numbers"
                return(1, strerr)
            elif f_x * fx1 < 0:
                root = (x_0, x_1)
                roots.append(root)
            else:
                root = None
            x_0 = x_1
            f_x = fx1
            x_1 = x_0 + delta
            fx1 = function(x_1)
            cont += 1
    return 0, roots, cont

print(incremental_searches(5, 1.5, 20))
