import unittest
import subprocess   
from ProductionCode.cl_code2 import *

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

        self.assertEqual(percentage_with_internet_access(country, self.data), "SystemExit: 0")


    def test_get_ratios(self):
        """Test for all ratios of education compared with gender
        when given a country"""

        ratio_1 = [1, 1, 1, 2]


        ratios = get_ratios(ratio_1)

        self.assertEqual([(1, 75), (2, 25)], ratios)
    
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
        
    def test_get_ratio(self):
        """Given a key and column, get_ratio returns how often the key appears
        in the column as a ratio"""
        
        column = [1, 1, 2, 2]
        key = 1
        
        rate = get_ratio(key, column)
        
        self.assertEqual(rate, 50)
        
    
    def test_get_column_index(self):
        """Given a column name and a dataset, returns the column's index"""
        
        col_name = "age"

        self.assertEqual(get_column_index(col_name), 7)

    def test_list_of_countries(self):
        """Testing if the function correctly returns the list of countries"""

        final_list = list_of_countries(self.data)

        self.assertEqual(final_list[0], "Afghanistan")

               
    def test_main(self):
        """Given a command-line argument, correctly parses it and returns the function's value"""
        
        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--internet_access_by_country", "Algeria"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "88.9 percent of Algeria has internet access.")
        code.terminate()
        
    
    def test_main_2(self):
        """Given a command-line argument, correctly parses it and returns the function's value"""
        
        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--education_levels_by_country_and_gender", "Peru"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = 'utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), "Education levels in Peru:\nFor females:\nPrimary school or less: 16.9 percent\nSecondary school: 74.1 percent\nTertiary education or more: 8.5 percent\nFor males:\nPrimary school or less: 13.6 percent\nSecondary school: 74.6 percent\nTertiary education or more: 11.6 percent")
        code.terminate()

    # have to change main to give this error message before this will work
    # def test_main_edge_case(self):
    #     code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--internet_access_by_country", "Franze"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = 'utf8')
    #     output, err = code.communicate()
    #     self.assertEqual(output.strip(), "Please enter a valid country. Hint: if the country is multiple words, enclose it in quotes.")
    #     code.terminate()
   
    
    def test_get_average_of_column(self):
        """Given a column of integers, returns the mean"""
        
        column = "age"
        country = "Argentina"
        
        average_age = get_average_of_column(country, column, self.data)
        
        self.assertEqual(average_age, 45.7)  

if __name__ == '__main__':
    unittest.main()

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

