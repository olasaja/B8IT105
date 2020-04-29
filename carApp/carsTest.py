# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:26:55 2020

@author: xx-Ol
"""


import unittest
import cars
import csv
import os.path

class TestCarApp(unittest.TestCase):
    
    def setUp(self):
        self.deal = cars.Dealership()
        self.deal.create_current_stock()#creating stock to test

    #check if rental processed
    def testRentProcessed(self):
        self.assertTrue(self.deal.process_rental)
        
    #check if save complete 
    def testSave(self): 
        self.assertTrue(os.path.isfile('carInventory.csv'))
    
    #set up car numbers test
    def CarStockTest(self, expected, car_list):  
        total = self.deal.count_stock(car_list)
        self.assertEqual(expected,total)
        
    #check number of petrol cars
    def testStockNumbersP(self): 
        self.CarStockTest(20, self.deal.getPetrolCars())
    
        #check number of electric cars
    def testStockNumbersE(self): 
        self.CarStockTest(6, self.deal.getElectricCars())
        
        #check number of diesel cars
    def testStockNumbersD(self): 
        self.CarStockTest(10, self.deal.getDieselCars())
        
        #check number of hybrid cars
    def testStockNumbersH(self): 
        self.CarStockTest(4, self.deal.getHybridCars())
                    
    #check if same number of rows written into csv (+header columns)
    def testRowNumersinCSV(self):
        self.deal.save_stock_state()
        expected = 41
        file = open('carInventory.csv')
        result = len(file.readlines())
        self.assertEqual(expected, result,"Incorrect number of rows in CSV")  
        file.close()
        
    # #test file load    
    # def testLoad(self):
    #     self.assertTrue(self.deal.load_car_stock())  
        
    # def testRent(self):
    #       car_list = self.deal.getElectricCars()
    #       self.assertEqual((self.deal.rent(car_list, 20)), 'Not enough cars in stock')
    
if __name__ == "__main__":
    unittest.main()      
    
'''

    assert: base assert allowing you to write your own assertions
    assertEqual(a, b): check a and b are equal
    assertNotEqual(a, b): check a and b are not equal
    assertIn(a, b): check that a is in the item b
    assertNotIn(a, b): check that a is not in the item b
    assertFalse(a): check that the value of a is False
    assertTrue(a): check the value of a is True
    assertIsInstance(a, TYPE): check that a is of type "TYPE"
    assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR

'''
