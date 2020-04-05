# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:58:47 2020

@author: 10540429
Unittest for wiki table 
"""

import wiki_table # program to be tested 
from bs4 import BeautifulSoup
import unittest
import csv
import os.path

class TestWikipedia(unittest.TestCase):   

#check if url response ok       
    def test_URL_response(self):
        self.assertEqual(wiki_table.response.status_code, 200 , "URL Response failed") 
    
#check if table exists on page 
    def test_contentExists(self):        
        content = wiki_table.soup.find_all('tbody')
        self.assertTrue(content,"Table does not exist") 
    
#check if object is beautifulSoup  
    def test_assert_true(self):
        self.assertTrue(type(self),"No object BeautifulSoup created") == BeautifulSoup
        
#confirm number of columns
    def testColumns(self):
        expected = 9
        result = len(wiki_table.get_content(wiki_table.soup)[0]) 
        self.assertEqual(expected,result,"Unexpected number of columns")
        
#confirm number of rows  
    def testRowNumers(self):
        expected = 220
        result = len(wiki_table.get_content(wiki_table.soup))
        self.assertEqual(expected, result,"Unexpected Number of rows")
        
#confirm csv created successfully  
    def test_csv_writer(self):
        self.assertTrue(os.path.isfile('wiki2.csv'),"CSV file not found in directory")
   
        
#check if same number of rows/columsn written into csv
#confirm number of rowsin csv
    def testRowNumersinCSV(self):
        expected = 220
        file = open('wiki2.csv')
        result = len(file.readlines())
        self.assertEqual(expected, result,"Incorrect number of rows in CSV")  
        file.close()
        
#confirm number of columnsin csv
    def testColumnsNumersinCSV(self):   
        expected = set({9})
        file = open('wiki2.csv')
        result = set([len(row) for row in csv.reader(file)])
        self.assertEqual(expected, result,"Incorrect number of columns in CSV")    
        file.close()
        
#compare csv output with table 
    def test_output(self):
        file = open('wiki2.csv')        
        csv_output = [row for row in csv.reader(file,quotechar='"',skipinitialspace=True)]
        bs_output = [row for row in wiki_table.get_content(wiki_table.soup)]
        self.assertEqual(csv_output,bs_output, "Values in CSV do not match")
        file.close()   
        
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
        

         