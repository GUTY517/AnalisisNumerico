#! /usr/bin/env python3
'''New Jacobi method implementation'''

from math import sqrt
from copy import copy
import numpy as np
from prettytable import PrettyTable
from numpy.linalg import inv, det, LinAlgError

def matrix_input():
    '''Console matrix input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix = np.array(entries).reshape(rows, columns)

    return matrix

def jacobi(x_0, matrix, vector):
    '''Returns Jacobi answers'''
    answer = []
    data_size = len(matrix)
    for i in range(data_size):
        results = 0
        for j in range(data_size):
            if j != i:
                results += matrix[i][j]*x_0[j]
        results = (vector[i] - results)/matrix[i][i]
        answer.append(results)
    return answer

def norm_2(x_0, x_1):
    '''Returns vectors norm'''
    results = 0
    data_size = len(x_0)
    for i in range(data_size):
        results += ((x_1[i] - x_0[i])**2)
    try:
        if sqrt(results):
            error = sqrt(results)
            return error, 0
    except OverflowError:
        return 0, 1

def main():
    '''Returns Jacobi answer and calculation table'''
    tolerance = float(input("Input tolerance: "))
    iterations = int(input("Input iterations: "))
    print("Input matrix in one line")
    matrix = matrix_input()
    print("Input vector in one line")
    vector = matrix_input()
    print("Input x0 in one line")
    x_0 = matrix_input()

    determinant = det(matrix)
    if determinant == 0:
        return(1, "Determinant is zero")
    try:
        inv(matrix)
    except LinAlgError:
        return 1, "Matrix is not invertible"

    title = ['iterations']
    answer = 0
    iterator = 0
    while answer < len(x_0):
        title.append(f"x{str(answer)}")
        answer += 1
    title.append("Error")
    table = PrettyTable(title)
    table.add_row([iterator] + x_0 + ["-"])
    error = tolerance + 1
    jacobi_response = jacobi(x_0, matrix, vector)
    while error > tolerance and iterator < iterations:
        x_1 = jacobi(x_0, matrix, vector)
        answer = norm_2(x_0, x_1)
        error = answer[0]
        err = answer[1]
        if err == 1:
            return 1, "Result is too big"
        iterator += 1
        table.add_row([iterator] + x_1 + [error])
        x_0 = copy(x_1)

    print("Answer (C) = ", jacobi_response)
    print()
    print(table)

main()

### Tests ###
# tolerance = 1e-7
# x_0 = [0,0,0,0]
# iterations = 100
# matrix = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
# vector = [1,1,1,1]
# print(main(tolerance,x_0,iterations,matrix,vector))
