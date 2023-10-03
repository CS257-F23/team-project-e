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
        
        self.assertAlmostEqual(ratio, 41.6)
    
    def test_percent_internet_access_edge_case1(self):
        """Edge case. Tests that percent_internet_access raises a ValueError if the user searches for a country that
        does not exist in the dataset"""

        country = "Nonexistent"

        self.assertEqual(percentage_with_internet_access(country, self.data), "Please enter a valid country. Hint: if the country is multiple words, enclose it in quotes.")

    def test_percent_internet_access_edge_case2(self):
        """Edge case. Tests that percent_internet_access raises a ValueError if the user searches for a country that
        does not exist in the dataset. Specifically, shows that country name abbreviations are not permitted"""

        country = "US"

        self.assertEqual(percentage_with_internet_access(country, self.data), "Please enter a valid country. Hint: if the country is multiple words, enclose it in quotes.")

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
        
        self.assertEqual
        self.assertRaises(ValueError, filter, key, col_name, self.data) # make it print out a correction statement instead of throwing an error
    
    def test_get_column_index(self):
        """Given a column name and a dataset, returns the column's index"""
        
        col_name = "age"

        self.assertEqual(get_column_index(col_name), 7)
        
    def test_education_level_by_gender(self):
        """Given a country, returns the levels of education obtained
        by its inhabitants, by gender, in a list format"""
        
        country = "Costa Rica"
        
        educ_levels = education_level_by_gender(country, self.data)
        
        self.assertEqual(educ_levels[0][0][1], 29.11)
        
        
        
    def test_main(self):
        """Given a command-line argument, correctly parses it and returns the function's value"""
        
        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--internet_access_by_country" "Algeria"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "88.9 percent of Algeria has internet access.")
        code.terminate()
        
    
    def test_main_2(self):
        """Given a command-line argument, correctly parses it and returns the function's value"""
        
        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--education_levels_by_country_and_gender", "Peru"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = 'utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "Education levels in Peru:\nFor females:\nPrimary school or less: 16.94 percent\nSecondary school: 74.09 percent\nTertiary education or more: 8.47 percent\nFor males:\nPrimary school or less: 13.57 percent\nSecondary school: 74.62 percent\nTertiary education or more: 11.56 percent")
        code.terminate()
    
        

if __name__ == '__main__':
    unittest.main()

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

