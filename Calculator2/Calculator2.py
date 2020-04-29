# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:45:10 2020

@author: 10540429

Assignment 3:
Create a Calculator class and CalculatorTest class that will implement 
functionality from a calculator using lists. Each function should 
use the lessons learned in the map, reduce, filter, and generator lecture.
    
"""
from functools import reduce

class Calculator:
    def __init__(self):
       self.x = []
       self.y = []

    def setX(self,x):
        self.x = x
        
    def setY(self,y):
        self.y = y
    
    def add(self,x,y):
        'Fuction to return sum of list of numbers'
        add = lambda x,y :x+y  
        return list(map(add, x, y))
    
    def sub(self, x,y):
        'Fuction to return difference of list of numbers'
        sub =  lambda x,y: x-y 
        return list(map(sub, x, y))
    
    def mult(self, x,y):
        'Function to return the product of list of numbers'
        mult = lambda x,y: x*y
        return list(map(mult, x, y))
    
    def div(self, x,y):
        'Function to return the dividend of list of numbers'
        try: 
            div = lambda x,y: x/y
            return list(map(div, x, y))
        except ZeroDivisionError:
            print('Division by Zero')
    
    def pwr(self, x,y):
        'Function to return the power of  list of numbers'
        pwr = lambda x,y: x**y
        return list(map(pwr, x, y))
    
    def sqr(self, x):
        'Function to return square of  list of numbers'
        sqr = lambda x : x**2 
        return list(map(sqr, x))
    
    def fact(self, x):    
        'Function to return factorial of  list of numbers'
        try: 
            fact = lambda x: 1 if x == 0 else reduce(lambda i, j : i*j, range(1, int(x+1)))
            return list(map(fact, x))
        except TypeError:
            print('Wrong input')
            
    def sqrt(self, x):
        'Function to return square root of a  list of numbers'
        sqrt = lambda x : x**(0.5)
        return list(map(sqrt, filter(lambda x:x > 0, x)))
    
    def operations_two(self, operation,x,y):
        if operation == 'A':
            result = self.add(x,y)
        if operation == 'S':
            result = self.sub(x,y)
        if operation == 'M':
            result = self.mult(x,y)
        if operation == 'D':
            result = self.div(x,y)
        if operation == 'P':
            result = self.pwr(x,y)
        return print('Result' + str(result))
            
    def operations_one(self, operation, x):
        if operation == 'SQ':
            result = self.sqr(x)
        if operation == 'FACT':
            result = self.fact(x)
        if operation == 'SQRT':
            result = self.sqrt(x) 
        return print('Result' + str(result))

    
    



                
    
    

