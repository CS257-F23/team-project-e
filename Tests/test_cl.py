import unittest
import subprocess   
from ProductionCode.cl_code2 import *

class test_dataset(unittest.TestCase):
    
    def setUp(self):
        self.data = load_data()

    def test_check_keyword_validity(self):

        keyword = "South Asia"
        column = "regionwb"

        keyword_validity = check_keyword_validity(keyword, column, self.data)

        self.assertEqual(keyword_validity, True)
    
    def test_check_keyword_validity_edge_case(self):
        
        keyword = "Earth"
        column = "regionwb"

        keyword_validity = check_keyword_validity(keyword, column, self.data)

        self.assertEqual(keyword_validity, False)
    
    def test_check_column_validity(self):

        column = "educ"

        column_validity = check_column_validity(column)

        self.assertEqual(column_validity, True)

    def test_check_column_validity_edge_case(self):

        column = "hemisphere"

        column_validity = check_column_validity(column)

        self.assertEqual(column_validity, False)
    
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

        country = "New York"

        country_list = list_of_countries(self.data)

        usage_message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\ninternet_access_by_country\naverage_age_of_country\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type '-h' in the command line."

        self.assertEqual(percentage_with_internet_access(country, self.data), usage_message)

    def test_percent_internet_access_edge_case2(self): 
        """Edge case. Tests that percent_internet_access raises a ValueError if the user searches for a country that
        does not exist in the dataset. Specifically, shows that country name abbreviations are not permitted"""

        country = "US"

        country_list = list_of_countries(self.data)

        usage_message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\ninternet_access_by_country\naverage_age_of_country\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type '-h' in the command line."

        self.assertEqual(percentage_with_internet_access(country, self.data), usage_message)


    """"
    def test_get_ratios(self): # we might not need this test if we don't even use the function
        ""Test for all ratios of education compared with gender
        when given a country""

        ratio_1 = [1, 1, 1, 2]


        ratios = get_ratios(ratio_1)

        self.assertEqual([(1, 75), (2, 25)], ratios)
    """
    
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
    
    def test_get_column_edge_case(self):

        column_name = "happiness"
        column = get_column(column_name, self.data)
        message = "Invalid column name."

        self.assertEqual(column, message)
    
    def test_filter(self):
        """Given a keyword, column, and dataset, filter returns
        the portion of the dataset where the column value matches the keyword"""
        
        key = "GEO"
        col_name = "economycode"
        
        new_data = filter(key, col_name, self.data)

        self.assertEqual(new_data[2][0], "Georgia")
    
    def test_filter_edge_case(self):

        key = "HEY"
        col_name = "economycode"
        message = "Invalid keyword or column name."

        new_data = filter(key, col_name, self.data)

        self.assertEqual(new_data, message)
        
    def test_get_ratio_of_key_in_column(self):
        """Given a key and column, get_ratio returns how often the key appears
        in the column as a ratio"""
        
        column = [1, 1, 2, 2]
        key = 1
        
        rate = get_ratio_of_key_in_column(key, column)
        
        self.assertEqual(rate, 50)
    
    def test_get_ratio_of_key_in_column_edge_case(self):

        key = "Chicago"
        column = "economy"

        rate = get_ratio_of_key_in_column(key, column)

        self.assertEqual(rate, 0.0)
        
    
    def test_get_column_index(self):
        """Given a column name and a dataset, returns the column's index"""
        
        col_name = "age"

        index = get_column_index(col_name)

        self.assertEqual(index, 7)
    
    def test_get_column_index_edge_case(self):
         
        col_name = "diet"

        index = get_column_index(col_name)
    
        self.assertEqual(index, "Invalid column name.")


    def test_list_of_countries(self):
        """Testing if the function correctly returns the list of countries"""

        final_list = list_of_countries(self.data)

        self.assertEqual(final_list[0], "Afghanistan")
    
    def test_string_of_countries(self):
        list_of_countries = ["Morocco", "Peru", "Russia"]
        string = string_of_countries(list_of_countries)

        result = "Morocco\nPeru\nRussia\n"

        self.assertEqual(string, result)
    
    def test_string_of_countries_edge_case(self):
        list_of_countries = []
        string = string_of_countries(list_of_countries)

        result = ""

        self.assertEqual(string, result)
    

    def test_get_average_of_column(self):
        """Given a column of integers, returns the mean"""
        
        country = "Argentina"
        column = "age"
        
        average_age = get_average_of_column(country, column, self.data)
        
        self.assertEqual(average_age, 45.6) 

    def test_get_average_of_column_edge_case(self):
         column = "age"
         country = "Canad"
         country_list = list_of_countries(self.data)
         message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\ninternet_access_by_country\naverage_age_of_country\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type '-h' in the command line."
    
         average_age = get_average_of_column(country, column, self.data)

         self.assertEqual(average_age, message)
    
    def test_calculate_averages(self):
        test_data = [1, 2, 3, 4]
        average = calculate_averages(test_data)
        result = 2.5

        self.assertEqual(average, result)
    
    def test_calculate_averages_edge_case(self):
        test_data = []
        average = calculate_averages(test_data)
        result = "Cannot calculate the average of no data."

        self.assertEqual(average, result)

    def test_usage_statement(self):
        data = []
        result = usage_statement(data)
        message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\ninternet_access_by_country\naverage_age_of_country\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\nTo view this information at any time, type '-h' in the command line."
   
        self.assertEqual(result, message)
    
    def test_main1(self):
        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code2.py", "--function", "internet_access_by_country", "--country", "Morocco"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()
        self.assertEqual(output.strip(), "83.0 percent of Morocco has internet access.")
        code.terminate()
    
    def test_main2(self):
        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code2.py", "--function", "average_age_of_country", "--country", "Kenya"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()
        self.assertEqual(output.strip(), "31.2 is the average age of people in Kenya.")
        code.terminate()
    

   
if __name__ == '__main__':
    unittest.main()
"""
    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

