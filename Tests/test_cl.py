import unittest
import subprocess   
from ProductionCode.cl_code import *

class test_dataset(unittest.TestCase):
    
    def setUp(self):
        self.data = load_data()
    
    def test_percent_internet_access1(self):
        """Given an existing country, percentage_with_internet_access returns the correct value"""
        
        country = "Afghanistan"
        ratio = percentage_with_internet_access(country, self.data)
        
        self.assertAlmostEqual(ratio, 19.8)

        
    def test_percent_internet_access2(self):
        """Given an existing country, percentage_with_internet_access returns the correct value"""
        
        country = "Nigeria"
        ratio = percentage_with_internet_access(country, self.data)
        
        self.assertAlmostEqual(ratio, 41.6, 1)
        
    def test_load_header(self):
        """Given the dataset, load_header loads the header"""
        header = load_header()
        
        self.assertEqual(header[-1], "year")
    
    def test_get_column(self):
        """Given a column name and a dataset, get_column returns thee
        column"""
        column_name = "regionwb"
        column = get_column(column_name, self.data)

        self.assertEqual(column[0], "South Asia")
    
    def test_filter(self):
        """Given a keyword, column, and dataset, filter returns
        the portion of the dataset where the column value matches the keyword"""
        
        key = "GEO"
        col_name = "economycode"
        
        new_data = filter(key, col_name, self.data)

        self.assertEqual(new_data[2][0], "Georgia")
        
    def test_filter_edge(self):
        """Given a column name that does not exist, filter returns an error"""
    
    def test_get_column_index(self):
        """Given a column name and a dataset, returns the column's index"""
        
        col_name = "age"

        self.assertEqual(get_column_index(col_name), 7)
        
    

if __name__ == '__main__':
    unittest.main()

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

