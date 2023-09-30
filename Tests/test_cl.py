import unittest
import subprocess   
from ProductionCode.cl_code import *

class test_dataset(unittest.TestCase):
    
    def setUp(self):
        load_data()
    
    def test_percent_internet_access(self):
        """Given an existing country, should return a value """
        
        country = "Afghanistan"
        ratio = percentage_with_internet_access(country)
        
        self.assertAlmostEqual(ratio, 19.7)
        

    
    
    
    

