# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:48:37 2020

@author: 10540429
"""
import csv

class Car(object):
    
    def __init__(self):
        self.__carID = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0
        self.__status = ''

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
        
    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status
    
    def setCarID(self, carID):
        self.__carID = carID

    def getCarID(self):
        return self.__carID
    
    def __str__(self):
        return "CarID:{0}, Car make:{1}, Car Model: {2}, Car Status: {3}".format(self.__carID, self.__make,self.__model,self.__status)

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
        
    
    def load_current_stock(self):
        with open('car_list.csv', newline = '') as file:
            reader = csv.reader(file)
            for line in reader:                
                if line[0] == 'Petrol':
                        car = PetrolCar()
                        car.setCarID(line[1])
                        car.setMake(line[2])
                        car.setModel(line[3])
                        car.setStatus(line[4])  
                        self.__petrol_cars.append(car)                      
                if line[0] == 'Electric':
                        car = ElectricCar()
                        car.setCarID(line[1])
                        car.setMake(line[2])
                        car.setModel(line[3])
                        car.setStatus(line[4]) 
                        self.__electric_cars.append(car)
                if line[0] == 'Diesel':
                        car = DieselCar()
                        car.setCarID(line[1])
                        car.setMake(line[2])
                        car.setModel(line[3])
                        car.setStatus(line[4]) 
                        self.__diesel_cars.append(car)  
                if line[0] == 'Hybrid':
                        car = HybridCar()
                        car.setCarID(line[1])
                        car.setMake(line[2])
                        car.setModel(line[3])
                        car.setStatus(line[4]) 
                        self.__hybrid_cars.append(car)  
                        
    def save_stock_state(self):
        car = ""
        csv_columns = ['carType','CarID', 'Make','Model','RentalStatus']
        with open('car_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(csv_columns) 
            for car in self.__petrol_cars:
                writer.writerow(('Petrol', car.getCarID(),car.getMake() ,car.getModel(),car.getStatus()))
            for car in self.__electric_cars:
                writer.writerow(('Electric', car.getCarID(),car.getMake() ,car.getModel(),car.getStatus())) 
            for car in self.__diesel_cars:
                writer.writerow(('Diesel',car.getCarID(),car.getMake(),car.getModel(),car.getStatus()))
            for car in self.__hybrid_cars:
                writer.writerow(('Hybrid', car.getCarID(),car.getMake() ,car.getModel(),car.getStatus()))
                
                        
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
    
    def count_available_stock(self,car_list):
        available = []
        for car in car_list: 
            if car.getStatus() == 'Available':
                available.append(car)
        return len(available)
                
    def stock_count(self):
        print('Number of total Petrol Cars : ' + str(self.count_stock(self.__petrol_cars)))
        print('Number of total Electric Cars : ' + str(self.count_stock(self.__electric_cars)))
        print('Number of total Diesel Cars : ' + str(self.count_stock(self.__diesel_cars)))
        print('Number of total Hybrid Cars : ' + str(self.count_stock(self.__hybrid_cars)))
    
    def stock_count_available(self):
        print('Number of available Petrol Cars : ' + str(self.count_available_stock(self.__petrol_cars)))
        print('Number of available Electric Cars : ' + str(self.count_available_stock(self.__electric_cars)))
        print('Number of available Diesel Cars : ' + str(self.count_available_stock(self.__diesel_cars)))
        print('Number of available Hybrid Cars : ' + str(self.count_available_stock(self.__hybrid_cars)))
        

    def rent(self, car_list, carID):
            for car in car_list:
                 if car.getCarID() == carID:
                    #print(car.getStatus())
                    car.setStatus('Rented')
                    print('Car rented. New Car status:' + str(car.getStatus()))
    
    def returnCar(self,car_list, carID):
        for car in car_list:
            if car.getCarID() == carID:
                #print(car.getStatus())
                car.setStatus('Available')
                print('Car Returned. New car status:' + str(car.getStatus()))
        
    def viewCarOptions(self,car_list):
        if car_list == 'P':
            for car in self.getPetrolCars():
                print(car)
        elif car_list == 'E':   
            for car in self.getElectricCars():
                print(car)
        elif car_list == 'D':   
            for car in self.getDieselCars():
                print(car)
        elif car_list == 'H':   
            for car in self.getHybridCars():
                print(car)
                
    def viewRentedCars(self,car_list):
        if car_list == 'P':
            for car in self.getPetrolCars():
                if car.getStatus() == 'Rented':
                    print(car)
        elif car_list == 'E':   
            for car in self.getElectricCars():
                if car.getStatus() == 'Rented':
                    print(car)
        elif car_list == 'D':   
            for car in self.getDieselCars():
                if car.getStatus() == 'Rented':
                    print(car)
        elif car_list == 'H':   
            for car in self.getHybridCars():
                if car.getStatus() == 'Rented':
                    print(car)
        
    def process_rental(self, car_list, carID):
        if car_list == 'P':
            self.rent(self.__petrol_cars,carID)
        elif car_list == 'E':   
            self.rent(self.__electric_cars,carID)
        elif car_list == 'D':   
            self.rent(self.__diesel_cars,carID)
        elif car_list == 'H':   
            self.rent(self.__hybrid_cars,carID)
        #self.stock_count()
        #self.stock_count_available()
            
    def process_return(self, car_list, carID):
        if car_list == 'P':
            self.returnCar(self.__petrol_cars,carID)
        elif car_list == 'E':   
            self.returnCar(self.__electric_cars,carID)
        elif car_list == 'D':   
            self.returnCar(self.__diesel_cars,carID)
        elif car_list == 'H':   
            self.returnCar(self.__hybrid_cars,carID)
        

                