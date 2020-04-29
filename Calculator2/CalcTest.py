# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:46:53 2020

@author: 10540429

CalculatorTest
"""


import unittest
import  Calculator2 as calc


class TestMyCalculator(unittest.TestCase):
    
    def setUp(self):
        self.cal = calc.Calculator()
        self.x = [-1,3,5,7]
        self.y = [-6,-4,6,15]
          
    def testAdd(self):
        expected_result = [-7, -1, 11, 22]
        self.assertEqual(self.cal.add(self.x,self.y),expected_result)
        
    def testSub(self):
        expected_result = [5, 7, -1, -8] 
        self.assertEqual(self.cal.sub(self.x,self.y),expected_result)
        
    def testMult(self):
        expected_result = [6, -12, 30, 105]
        self.assertEqual(self.cal.mult(self.x,self.y),expected_result)
        
    def testDiv(self):
        expected_result = [0.16666666666666666, -0.75, 0.8333333333333334, 0.4666666666666667]
        self.assertEqual(self.cal.div(self.x,self.y),expected_result)
    
    def testDivZero(self):
        expected_result = None
        self.assertEqual(self.cal.div(self.x,[0,5,6,0]),expected_result)
        
    def testPwr(self):
        expected_result =  [1.0, 0.012345679012345678, 15625, 4747561509943]
        self.assertEqual(self.cal.pwr(self.x,self.y),expected_result)
        
    def testSqr(self):
        x = [2,6,8]
        expected_result =  [4, 36, 64]
        self.assertEqual(self.cal.sqr(x),expected_result)

    def testFactorial(self):
        expected_result = [40320, 24]
        self.assertEqual(self.cal.fact([8,4]),expected_result)
    
    def testSqrRt(self):
        expected_result = [3.0, 5.0]
        x = [9, 25]
        self.assertEqual(self.cal.sqrt(x),expected_result)

        
    def testNegFactorial(self):
        expected_result = None
        self.assertEqual(self.cal.fact([-8,-4]),expected_result)
      
    def testFactorialFloat(self):
        expected_result = [40320, 24]
        self.assertEqual(self.cal.fact([8.0,4.0]),expected_result)

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