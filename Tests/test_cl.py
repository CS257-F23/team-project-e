import unittest
import subprocess   
from ProductionCode.cl_code import *

class test_dataset(unittest.TestCase): 
    
    def setUp(self):
        """Loads the data so that the tests can run. """

        self.data = Dataset()

    def test_check_keyword_validity(self):
        """Test checking that function check_keyboard_validity returns True for a valid input"""

        keyword = "South Asia"
        column = "regionwb"

        keyword_validity = self.data.check_keyword_validity(keyword, column, self.data)

        self.assertEqual(keyword_validity, True)
    
    def test_check_keyword_validity_edge_case(self):
        """Test checking that check_keyboard_validity returns False for an invalid input"""

        keyword = "Earth"
        column = "regionwb"

        keyword_validity = self.data.check_keyword_validity(keyword, column, self.data)

        self.assertEqual(keyword_validity, False)
    
    def test_check_column_validity(self):
        """Test checking that check_column_validity returns True for a valid input"""

        column = "educ"

        column_validity = self.data.check_column_validity(column)

        self.assertEqual(column_validity, True)

    def test_check_column_validity_edge_case(self):
        """Test checking that check_column_validity returns False for an invalid input"""

        column = "hemisphere"

        column_validity = check_column_validity(column)

        self.assertEqual(column_validity, False)
    
    def test_load_header(self):
        """Given the dataset, load_header loads the header string"""

        header = load_header()
        
        self.assertEqual(header[-1], "year")
    
    def test_get_column(self):
        """Given a column name and a dataset, get_column returns thee
        column as a string"""

        column_name = "regionwb"
        column = get_column(column_name, self.data)

        self.assertEqual(column[0], "South Asia")
    
    def test_get_column_edge_case(self):
        """Edge case testing that get_column correctly identifies that an invalid column string
        has been given"""

        column_name = "happiness"
        column = get_column(column_name, self.data)
        message = "Invalid column name."

        self.assertEqual(column, message)
    
    def test_filter(self):
        """Given a keyword, column, and dataset, filter returns
        the portion of the dataset where the column value matches the keyword string"""
        
        key = "GEO"
        col_name = "economycode"
        
        new_data = filter(key, col_name, self.data)

        self.assertEqual(new_data[2][0], "Georgia")
    
    def test_filter_edge_case(self):
        """Edge case testing that an invalid key for filter() correctly identifies
        an invalid key string"""

        key = "HEY"
        col_name = "economycode"
        message = "Invalid keyword or column name."

        new_data = filter(key, col_name, self.data)

        self.assertEqual(new_data, message)
        
    def test_get_ratio_of_key_in_column(self):
        """Given a key and column, get_ratio returns how often the key appears
        in the column as a integer ratio"""
        
        column = [1, 1, 2, 2]
        key = 1
        
        rate = get_ratio_of_key_in_column(key, column)
        
        self.assertEqual(rate, 50)
    
    def test_get_ratio_of_key_in_column_edge_case(self):
        """Test checking the edge case in which an incorrect key name string 
        has been given. Should return a 0.0 integer"""

        key = "Chicago"
        column = "economy"

        rate = get_ratio_of_key_in_column(key, column)

        self.assertEqual(rate, 0.0)
        
    
    def test_get_column_index(self):
        """Given a column name string and a dataset, returns the column's index as an integer"""
        
        col_name = "age"

        index = get_column_index(col_name)

        self.assertEqual(index, 7)
    
    def test_get_column_index_edge_case(self):
        """Test checking that get_column_index correclty identifies when an
        invalid column name string has been given."""

        col_name = "diet"

        index = get_column_index(col_name)
    
        self.assertEqual(index, "Invalid column name.")


    def test_list_of_countries(self):
        """Testing if the function correctly returns the list of countries
        from the data as a string"""

        final_list = list_of_countries(self.data)

        self.assertEqual(final_list[0], "Afghanistan")
    
    def test_string_of_countries(self):
        """Test identifying whether string_of_countries correctly returns
        a string of countries"""

        list_of_countries = ["Morocco", "Peru", "Russia"]
        string = string_of_countries(list_of_countries)

        result = "Morocco\nPeru\nRussia\n"

        self.assertEqual(string, result)
    
    def test_string_of_countries_edge_case(self):
        """Test identifying whether string_of_countries correctly returns
        an empty string for the edge case of no countries in the string"""

        list_of_countries = []
        string = string_of_countries(list_of_countries)

        result = ""

        self.assertEqual(string, result)
    

    def test_get_average_of_column(self):
        """Given a column of integers, returns the mean as an integer"""
        
        country = "Argentina"
        column = "age"
        
        average_age = get_average_of_column(country, column, self.data)
        
        self.assertEqual(average_age, 45.6) 

    def test_get_average_of_column_edge_case(self):
        """Test identifying whether get_average_of_column will correclty identify when an 
        incorrect country string has been given"""

        column = "age"
        country = "Canad"
        country_list = list_of_countries(self.data)
        message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        average_age = get_average_of_column(country, column, self.data)

        self.assertEqual(average_age, message)
    
    def test_calculate_averages(self):
        """Test identifying whether calculate_averages correctly calculates averages of integers
        Should output an integer"""

        test_data = [1, 2, 3, 4]
        average = calculate_averages(test_data)
        result = 2.5

        self.assertEqual(average, result)
    
    def test_calculate_averages_edge_case(self):
        """Test identifying whether calculate_averages will correctly return message if no data is given"""

        test_data = []
        average = calculate_averages(test_data)
        result = "Cannot calculate the average of no data."

        self.assertEqual(average, result)
    
    def test_has_financial_account_single_country(self):
        """Tests that has_financial_account_single_country correctly returns the percentage of a 
        country that has a financial account. """

        country = "Greece"
        financial_account_single_country = has_financial_account_single_country(country, self.data)
        
        result = 97.6

        self.assertEqual(financial_account_single_country, result)
    
    def test_has_financial_account_single_country_edge_case(self):
        """Tests that has_financial_account_single_country correctly returns the usage statement if the
        user enters an invalid country. """

        country = "Narnia"
        financial_account_single_country = has_financial_account_single_country(country, self.data)
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(financial_account_single_country, result)
    
    def test_has_financial_account_global(self):
        """Tests that has_financial_account_global correctly returns the percentage of people in all 
        countries worldwide that have a financial account. """

        financial_account_global = has_financial_account_global(self.data)

        result = 65.8

        self.assertEqual(financial_account_global, result)
    
    def test_format_financial_comparison(self):
        """Tests that format_financial_comparison correctly returns a formatted string with
        the results of the financial comparison functions. """

        country = "Greece"
        country_result = has_financial_account_single_country(country, self.data)
        global_result = has_financial_account_global(self.data)
        format_comparison = format_financial_comparison(country, country_result, global_result)

        result = "Percentage of people in Greece who have a financial account: 97.6\nPercentage of people worldwide who have a financial account: 65.8"
        
        self.assertEqual(format_comparison, result)
    
    def test_internet_access_by_country(self):
        """Tests that internet_access_by_country correctly returns the percentage of a country
        that has internet access. """

        country = "Zambia"
        internet_access = internet_access_by_country(country, self.data)

        result = 26.5

        self.assertEqual(internet_access, result)
    
    def test_internet_access_by_country_edge_case(self):
        """Tests that internet_access_by_country correctly returns the usage statement if
        the user enter an invalid country. """

        country = "Maine"
        internet_access = internet_access_by_country(country, self.data)
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(internet_access, result)
    
    def test_tertiary_education_by_country(self):
        """Tests that tertiary_education_by_country correctly returns the percentage of a country
        that has attained tertiary (college) education. """

        country = "Ireland"
        tertiary_education = tertiary_education_by_country(country, self.data)

        result = 45.6

        self.assertEqual(tertiary_education, result)
    
    def test_tertiary_education_by_country_edge_case(self):
        """Tests that tertiary_education_by_country correctly returns the usage statement
        if the user enters an invalid country. """

        country = ""
        tertiary_education = tertiary_education_by_country(country, self.data)
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(tertiary_education, result)
    
    def test_population_by_country(self):
        """Tests that population_by_country correctly returns the population of a country. """

        country = "China"
        population = population_by_country(country, self.data)

        result = "1153772544"

        self.assertEqual(population, result) 
    
    def test_population_by_country_edge_case(self):
        """Tests that population_by_country_edge_case correctly returns the usage statement if the user
        enters an invalid country. """

        country = "London"
        population = population_by_country(country, self.data)
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(population, result)
    
    def test_employment_by_country(self):
        """Tests that employment_by_country correctly returns the percentage of a country that is employed. """

        country = "Iceland"
        employment = employment_by_country(country, self.data)

        result = 73.3

        self.assertEqual(employment, result)
    
    def test_employment_by_country_edge_case(self):
        """Tests that employment_by_country correctly returns the usage statement if the
        user enters an invalid country. """

        country = "iceland"
        employment = employment_by_country(country, self.data)
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(employment, result)
    
    def test_four_stat_summary_by_country(self):
        """Tests that four_stat_summary_by_country correctly returns a formatted string with the
        results of the four statistics of interest for the given country. """

        country = "United States"
        summary = four_stat_summary_by_country(country, self.data)

        result = "Percentage of United States with internet access: 94.3\nPercentage of United States that has attained tertiary education or higher: 43.9\nPopulation of United States: 268952128\nPercentage of United States that is employed: 63.1"
        
        self.assertEqual(summary, result)

    def test_average_age_by_country(self):
        """Tests that average_age_by_country correctly returns the average age of a country. """

        country = "Brazil"
        average_age = average_age_by_country(country, self.data)

        result = 41.2

        self.assertEqual(average_age, result)
    
    def test_average_age_by_country_edge_case(self):
        """Tests that average_age_by_country correctly returns the usage statement if the user enters
        an invalid country. """

        country = "North America"
        average_age = average_age_by_country(country, self.data)
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(average_age, result)
    
    def test_financial_worry_education_by_country(self):
        """Tests that financial_worry_education_by_country correctly returns the percentage of
        a country that is worried about financing their education. """

        country = "Australia"
        comparison = financial_worry_education_by_country(country, self.data)

        result = 8.8

        self.assertEqual(comparison, result)
    
    def test_financial_worry_education_by_country_edge_case(self):
        """Tests that financial_worry_education_by_country correctly returns the usage statement
        if the user enters an invalid country. """

        country = "Perth"
        comparison = financial_worry_education_by_country(country, self.data)
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
       
        self.assertEqual(comparison, result)
    
    def test_format_age_financial_worry_by_education_summary(self):
        """Tests that format_age_financial_worry_by_education_summary correctly returns the formatted
        results of the age and financial worry comparison functions. """

        country = "Uzbekistan"
        formatted_comparison = format_age_financial_worry_by_education_summary(country, self.data)

        result = "Average age of Uzbekistan: 42.4\nPercentage of people in Uzbekistan who are worried about financing their education: 34.3"
        
        self.assertEqual(formatted_comparison, result)
   
    def test_usage_statement(self):
        """Test identifying whether usage_statement will return correct message when no data is given"""

        data = []
        result = usage_statement(data)

        message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(result, message)
     
    def test_main_four_stat_summary(self):
        """Tests the main function when the function tag is associated with four_stat_summary. """

        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--function", "four_stat_summary", "--country", "Canada"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()

        result = "Percentage of Canada with internet access: 95.2\nPercentage of Canada that has attained tertiary education or higher: 41.5\nPopulation of Canada: 32009816\nPercentage of Canada that is employed: 62.3"
        
        self.assertEqual(output.strip(), result)

        code.terminate()
    
    def test_main_financial_account(self):
        """Tests the main function when the function tag is associated with financial_account_summary. """

        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--function", "financial_account_comparison", "--country", "Senegal"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()

        result = "Percentage of people in Senegal who have a financial account: 33.9\nPercentage of people worldwide who have a financial account: 65.8"
        
        self.assertEqual(output.strip(), result)

        code.terminate()
    
    def test_main_age_education(self):
        """Tests the main function when the function tag is associated with age_education_worry_comparison. """

        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--function", "age_education_worry_comparison", "--country", "Vietnam"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()

        result = "Average age of Vietnam: 38.0\nPercentage of people in Vietnam who are worried about financing their education: 40.3"
        
        self.assertEqual(output.strip(), result)

        code.terminate()
    
    def test_main_edge_case(self):
        """Tests that the main function will print out the usage statement if the user does not enter a function argument. """

        code = subprocess.Popen(["python3", "-u", "ProductionCode/cl_code.py", "--function", "", "--country", "Peru"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()
        
        country_list = list_of_countries(self.data)

        result = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(output.strip(), result)

        code.terminate()

   
if __name__ == '__main__':
    unittest.main()

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

