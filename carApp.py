# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:30:38 2020

@author: xx-Ol
"""
from  cars import Car, ElectricCar, PetrolCar,HybridCar, DieselCar, Dealership 

program = Dealership()
#program.create_current_stock()
#program.save_stock_state()   
program.load_car_stock()

def main():
    print('This is a car rental place')
    msg = ("What would you like to do?\n"
            
            "1.Rent a car\n"
            "2.Return a car\n"
            "3.Check stock\n"
            "Any other key to exit."
            )

    answer = input(msg)
    while answer == '1' or answer == '2' or answer == '3':
        if answer == '1':
            answer = input('what type would you like? p/e/d/h').upper()
            amount = int(input('how many would you like?'))
            program.process_rental(answer,amount)   
            program.save_stock_state()                                 
        elif answer == '2':
            type = input('what type of car do you want to return p/e/d/h').upper()
            program.returnCar(type) 
            program.save_stock_state()
        elif answer == '3':
            program.stock_count() 

        answer = input(msg)
        
        
main()




