#! /usr/bin/env python3
'''New Jacobi method implementation'''

from math import sqrt
import numpy as np
from prettytable import PrettyTable
from numpy.linalg import inv, det, LinAlgError

def matrix_input():
    '''Console matrix_a input'''
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(float, input().split()))
    matrix_a = np.array(entries).reshape(rows, columns)

    return matrix_a

def jacobi(x_0, matrix_a, vector):
    '''Returns Jacobi answers'''
    answer = []
    data_size = len(matrix_a)
    for i in range(data_size):
        results = 0
        for j in range(data_size):
            if j != i:
                results += matrix_a[i][j]*x_0[j]
        results = (vector[i] - results)/matrix_a[i][i]
        answer.append(results)
    return answer

def new_norm(x_0, x_1):
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
    matrix_a = matrix_input()
    vector = matrix_input()
    x_0 = matrix_input()

    determinant = det(matrix_a)
    if determinant == 0:
        return(1, "Determinant is zero")
    try:
        inv(matrix_a)
    except LinAlgError:
        return 1, "Matrix is not invertible"

    title = ['n']
    answer = 0
    iterator = 0
    while answer < len(x_0):
        title.append(f"x{str(answer)}")
        answer += 1
    title.append("Error")
    table = PrettyTable(title)
    table.add_row([iterator] + x_0 + ["-"])
    error = tolerance + 1
    jacobi_response = jacobi(x_0, matrix_a, vector)
    while error > tolerance and iterator < iterations:
        x_1 = jacobi(x_0, matrix_a, vector)
        answer = new_norm(x_0,x_1)
        error = answer[0]
        err = answer[1]
        if err == 1:
            return 1, "Result is too big"
        iterator += 1
        table.add_row([iterator] + x_1 + [error])
    print("Answer (C) = ", jacobi_response)
    print()
    return table

print(main())

### Tests ###
# matrix_a = np.array([[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]])
# vector = np.array([[1], [1], [1], [1]])
# tolerance = 1e-7
# x_0 = [0,0,0,0]
# iterations = 100
# matrix_a = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30]]
# vector = [1,1,1,1]
# print(main(tolerance,x_0,iterations,matrix_a,vector))