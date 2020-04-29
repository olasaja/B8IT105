# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:25:49 2020

@author: 10540429
"""

from  Calculator2 import Calculator

cal = Calculator()

def menu():
    print('Options menu:\n'
        'A to add,\n' 
        'S to subtract\n'
        'M to multiply\n'
        'D to divide\n'
        'P to power\n'
        'SQ to square\n'
        'FACT for factorial\n'
        'SQRT for square route')

def main():   
    menu()
    calculate = input('Do you want to calculate something?Y to continue').upper()
    while calculate== 'Y':
        op = input('What are you trying to do?').upper() 
        n = int(input("Enter number of elements : ")) 
        x = list(map(float,input("\nEnter the numbers separated by comma: ").strip().split(',')))[:n]   
        cal.setX(x)
        if op in['SQ', 'FACT','SQRT']:   
            cal.operations_one(op,x)
        else: 
            y = list(map(float,input("\nEnter the numbers separated by comma: ").strip().split(',')))[:n] 
            cal.setY(y)
            cal.operations_two(op,x,y)

main()      