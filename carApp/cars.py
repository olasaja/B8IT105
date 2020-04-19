# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:48:37 2020

@author: xx-Ol
"""
import csv

class Car(object):
    
    def __init__(self):
        self.__make = ''
        self.__model = ''
        self.__mileage = 0

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def getMileage(self):
        return self.__mileage

    def distance_traveled(self, km_travelled):
        self.__mileage = self.__mileage + km_travelled

class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__drivingRange= ""
        
    def getRange(self):
        return self.__drivingRange 
    
    def setRange(self, drivingRange):
        self.__drivingRange = drivingRange

class PetrolCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize


class DieselCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
        
class HybridCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        

class Dealership(object):

    def __init__(self):

        self.__petrol_cars = []
        self.__electric_cars = []
        self.__diesel_cars = []
        self.__hybrid_cars = []
        
    def create_current_stock(self):
        for i in range(1, 21): #20 petrol cars
            self.__petrol_cars.append(PetrolCar())
        for i in range(1, 7): #6 electric
            self.__electric_cars.append(ElectricCar()) 
        for i in range(1, 11): #10 diesel
            self.__diesel_cars.append(DieselCar())   
        for i in range(1, 5): #4 hybrid
            self.__hybrid_cars.append(HybridCar())
        
    def getPetrolCars(self):
        return self.__petrol_cars

    def getElectricCars(self):
        return self.__electric_cars

    def getDieselCars(self):
        return self.__diesel_cars    
    
    def getHybridCars(self):
        return self.__hybrid_cars        
            
    def count_stock(self,car_list):
        return len(car_list)
        
    def stock_count(self):
        print('Number of Petrol Cars : ' + str(self.count_stock(self.__petrol_cars)))
        print('Number of Electric Cars : ' + str(self.count_stock(self.__electric_cars)))
        print('Number of Diesel Cars : ' + str(self.count_stock(self.__diesel_cars)))
        print('Number of Hybrid Cars : ' + str(self.count_stock(self.__hybrid_cars)))
    
    def save_stock_state(self):
        line = ""
        csv_columns = ['carType','CarObject']
        with open('carInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(csv_columns) 
            for line in self.__petrol_cars:
                writer.writerow(('petrol', line))
            for line in self.__electric_cars:
                writer.writerow(('electric', line))  
            for line in self.__diesel_cars:
                writer.writerow(('diesel', line))
            for line in self.__hybrid_cars:
                writer.writerow(('hybrid', line))
                
    def load_car_stock(self):
        with open('carInventory.csv', newline = '') as file:
            car_list = csv.reader(file)
            for car in car_list:
                if car[0] == 'petrol':
                    self.__petrol_cars.append(car[1])    
                if car[0] == 'electric':
                    self.__electric_cars.append(car[1])  
                if car[0] == 'diesel':
                    self.__diesel_cars.append(car[1])  
                if car[0] == 'hybrid':
                    self.__hybrid_cars.append(car[1])                         

    def rent(self, car_list, amount):
        if self.count_stock(car_list) < amount:
            return print('Not enough cars in stock')      
        else: 
            total = 0
            while total < amount:
               car_list.pop()
               total = total + 1
    
    def returnCar(self, type):
        #type = input('what type of car do you want to return p/e/d/h').upper()
        if type == 'P':
            self.__petrol_cars.append(PetrolCar())
        elif type == 'E':
            self.__electric_cars.append(ElectricCar())
        elif type == 'D':
            self.__diesel_cars.append(DieselCar())
        elif type == 'H':
            self.__hybrid_cars.append(HybridCar())
        self.stock_count()
        
    def process_rental(self,answer,amount):
        #answer = input('what type would you like? p/e/d/h').lower()
        #amount = int(input('how many would you like?'))
        if answer == 'P':
            self.rent(self.__petrol_cars, amount)
        elif answer == 'E':   
            self.rent(self.__electric_cars, amount)
        elif answer == 'D':   
            self.rent(self.__diesel_cars, amount)
        elif answer == 'H':   
            self.rent(self.__hybrid_cars, amount)
        self.stock_count()
        

                
