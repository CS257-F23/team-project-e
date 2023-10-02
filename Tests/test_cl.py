import unittest
import subprocess   
from ProductionCode.cl_code import *

class test_dataset(unittest.TestCase):
    
    def setUp(self):
        data = load_data()         
    
    def test_percent_internet_access1(self):
        """Given an existing country, percentage_with_internet_access returns the correct value"""
        
        country = "Afghanistan"
        ratio = percentage_with_internet_access(country, data)
        
        self.assertAlmostEqual(ratio, 19.7)
        
    def test_percent_internet_access2(self):
        """Given an existing country, percentage_with_internet_access returns the correct value"""
        
        country = "Nigeria"
        ratio = percentage_with_internet_access(country, data)
        
        self.assertAlmostEqual(ratio, 41.6)
        
    def test_load_header(self):
        """Given the dataset, load_header correctly loads the header"""
        header = load_header()
        
        self.assertEqual(header[-1], "year")
    
    def test_get_column(self):
        """Given a column name and a dataset, get_column correctly returns the
        column"""
    
    def test_filter(self):
        """Given a keyword, column, and dataset, filter correctly returns
        the portion of the dataset where the column value matches the keyword"""
        
        key = "GEO"
        col_name = "economycode"
        
        new_data = filter(key, col_name, data)
        
        #self.assertEqual(new_data[0])
        
    
    
    def test_get_column_index(self):
        """Given a column name and a dataset, correctly returns the column's name"""
        
        
    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

