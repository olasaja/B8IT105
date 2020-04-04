# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:58:47 2020

@author: xx-Ol
"""

import wiki_table # program to be tested 
from bs4 import BeautifulSoup
import unittest
import os.path

class TestWikipedia(unittest.TestCase):   

#check if url code 200
    def test_URL_response(self):
        self.assertEqual(wiki_table.response.status_code, 200)  
    
#check if table exists on page 
    def test_contentExists(self):        
        content = wiki_table.soup.find_all('tbody')
        self.assertTrue(content)
        
    
#check if object is beautifulSoup  
    def test_assert_true(self):
          self.assertTrue(type(self)) == BeautifulSoup
   
#confirm number of columns
    def testColumns(self):
        expected = 9
        result = len(wiki_table.get_content(wiki_table.soup)[0]) 
        self.assertEqual(expected,result)
        
#confirm number of rows  
    def testRowNumers(self):
        expected = 220
        result = len(wiki_table.get_content(wiki_table.soup))
        self.assertEqual(expected, result)
        
        
#confirm csv created successfully  
    def test_csv_writer(self):
        self.assertTrue(os.path.isfile('wiki2.csv'))
        
#check if same number of rows/columsn written into csv
#confirm number of rowsin csv
    def testRowNumersinCSV(self):
        expected = 220
        file = open('wiki2.csv')
        result = len(file.readlines())
        self.assertEqual(expected, result)  
        file.close()
        
# #confirm number of columnsin csv
#     def testColumnsNumersinCSV(self):        
#         expected = 9
#         result = len([row for row in open('wiki2.csv')][0])
#         self.assertEqual(expected, result)    

#compare csv output with table 
#test failed 
    # def test_output(self):         
    #     self.assertEqual([row for row in open('wiki2.csv')],[row for row in wiki_table.rows])
           
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
        

         