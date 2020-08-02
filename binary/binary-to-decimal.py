#! /usr/bin/env python3

def menu():
    pass

def binToDec():
    value = input("Input binary number: ")
    try:
        whole, decimal = value.split(".")
        binary_num = list(whole)
        binary_decimal = list(decimal)
        whole_value = 0
        decimal_value = 0
    
        # Convertion before point
        for i in range(len(binary_num)):
            digit = binary_num.pop()
            if digit == '1':
                whole_value = whole_value + pow(2,i)

        # Convertion after point
        for j in range(len(binary_decimal),0,-1):
            decimal_digit = binary_decimal.pop()
            if decimal_digit == '1':
                decimal_value = decimal_value + pow(2,(j*-1))
        print("Decimal number: ", str(whole_value)+"."+str(decimal_value).split(".")[1])
    except ValueError:
        whole = value
        binary_num = list(whole)
        whole_value = 0
    
        # Convertion before point
        for i in range(len(binary_num)):
            digit = binary_num.pop()
            if digit == '1':
                whole_value = whole_value + pow(2,i)
        print("Decimal number: ", whole_value)

binToDec()
