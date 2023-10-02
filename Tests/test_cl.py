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
        
        self.assertAlmostEqual(ratio, 20)

        
    def test_percent_internet_access2(self):
        """Given an existing country, percentage_with_internet_access returns the correct value"""
        
        country = "Nigeria"
        ratio = percentage_with_internet_access(country, self.data)
        
        self.assertAlmostEqual(ratio, 42)
    
    def test_percent_internet_access_edge_case1(self):
        """Edge case. Tests that percent_internet_access raises a ValueError if the user searches for a country that
        does not exist in the dataset"""

        country = "Nonexistent"

        self.assertRaises(ZeroDivisionError, percentage_with_internet_access, country, self.data)

    def test_percent_internet_access_edge_case2(self):
        """Edge case. Tests that percent_internet_access raises a ValueError if the user searches for a country that
        does not exist in the dataset. Specifically, shows that country name abbreviations are not permitted"""

        country = "US"

        self.assertRaises(ZeroDivisionError, percentage_with_internet_access, country, self.data)
    
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
        
        col_name = "Group E"
        key = "Albert"
        
        self.assertRaises(ValueError, filter, key, col_name, self.data)
    
    def test_get_column_index(self):
        """Given a column name and a dataset, returns the column's index"""
        
        col_name = "age"

        self.assertEqual(get_column_index(col_name), 7)
        
    def test_education_level_by_gender(self):
        """Given a country, returns the levels of education obtained
        by its inhabitants, by gender, in a list format"""
        
        country = "Costa Rica"
        
        educ_levels = education_level_by_gender(country, self.data)
        
        # For some reason, need to print result to pass the test. Ask about later.
        print(educ_levels)
        
        self.assertEqual(educ_levels[0][0], 0.28)
        
        
        
    """def test_main(self):
        code = subprocess.Popen(["python3", "-u", "Tests/test_cl.py", "Algeria"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "88.9 percent of Algeria has internet access.")
        code.terminate()
    
    def test_main_2(self):
        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--education_levels_by_country", "Peru"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = 'utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "Education levels in Peru:\nPrimary school or less: 15.6 percent\nSecondary school: 74.3 percent\nTertiary education or more: 9.7 percent")
        code.terminate()

if __name__ == '__main__':
    unittest.main()

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

