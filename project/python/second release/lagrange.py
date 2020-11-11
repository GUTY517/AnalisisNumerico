#! /usr/bin/env python3
'''Lagrange method implementation'''

from sympy import Symbol, expand, factor, init_printing


def lagrange(value, j, matrix):
    '''Lagrange method'''
    init_printing(use_unicode=True)
    x_symbol = Symbol("x")
    checker = 0
    expansion = 1
    divisor = 1
    while checker < len(matrix):
        if checker != j:
            divisor = divisor * (matrix[j][0] - matrix[checker][0])
        checker += 1
    checker = 0
    while checker < len(matrix):
        if checker != j:
            polynomial = expand(x_symbol - matrix[checker][0])
            expansion = expand(expansion * polynomial)
        checker += 1
    polynomial = factor(expansion/divisor)
    lagrange_answer = polynomial.evalf(subs={x_symbol: value})
    return polynomial, lagrange_answer


def main():
    '''Data input and method execution'''
    x_values = [float(item) for item in input(
        "Input X values separated by space: ").split()]
    y_values = [float(item) for item in input(
        "Input Y values separated by space: ").split()]
    data = list(map(lambda x, y: [x, y], x_values, y_values))

    x_size = len(x_values)
    data_size = len(data)
    for i in range(x_size):
        polynomial_ecuation = 0
        answer = 0
        for j in range(data_size):
            lagrange_answer = lagrange(x_values[i], j, data)
            answer += lagrange_answer[1]*data[j][1]
            polynomial_ecuation += lagrange_answer[0]*data[j][1]
        print(f"Ecuation {i+1}:\n {polynomial_ecuation} = {answer}")


main()
