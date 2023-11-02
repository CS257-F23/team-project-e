import unittest
import subprocess   
from cl_code import *

class TestDataset(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        """Loads the data once for the entire test suite."""

        cls.data = Dataset()
        cls.data.connect()

    def test_check_keyword_validity(self):
        """Test checking that function check_keyboard_validity returns True for a valid input"""

        keyword = "South Asia"
        column = "regionwb"

        keyword_validity = self.data.check_keyword_validity(keyword)

        self.assertEqual(keyword_validity, True)
    
    def test_check_keyword_validity_edge_case(self):
        """Test checking that check_keyboard_validity returns False for an invalid input"""

        keyword = "Earth"
        column = "regionwb"

        keyword_validity = self.data.check_keyword_validity(keyword)

        self.assertEqual(keyword_validity, False)

    def test_list_of_countries(self):
        """Testing if the function correctly returns the list of countries
        from the data as a string"""

        final_list = self.data.list_of_countries()

        self.assertEqual(final_list[0], ("Afghanistan",) )
    
    def test_string_of_countries(self):
        """Test identifying whether string_of_countries correctly returns
        a string of countries"""

        string = self.data.string_of_countries()
        part_string = string[0:11]

        result = "Afghanistan"

        self.assertEqual(result, part_string)
    
    def test_has_financial_account_single_country(self):
        """Tests that has_financial_account_single_country correctly returns the percentage of a 
        country that has a financial account. """

        country = "Greece"
        financial_account_single_country = self.data.has_financial_account_single_country(country)
        
        result = 97.6

        self.assertEqual(financial_account_single_country, result)
    
    def test_has_financial_account_single_country_edge_case(self):
        """Tests that has_financial_account_single_country correctly returns the usage statement if the
        user enters an invalid country. """

        country = "Narnia"
        financial_account_single_country = self.data.has_financial_account_single_country(country)

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."

        self.assertEqual(financial_account_single_country, message)
    
    def test_has_financial_account_global(self):
        """Tests that has_financial_account_global correctly returns the percentage of people in all 
        countries worldwide that have a financial account. """

        financial_account_global = self.data.has_financial_account_global()

        result = 65.8

        self.assertEqual(financial_account_global, result)
    
    def test_format_financial_comparison(self):
        """Tests that format_financial_comparison correctly returns a formatted string with
        the results of the financial comparison functions. """

        country = "Greece"
        format_comparison = self.data.format_financial_comparison(country)

        result = "Percentage of people in Greece who have a financial account: 97.6\nPercentage of people worldwide who have a financial account: 65.8"
        
        self.assertEqual(format_comparison, result)
    
    def test_internet_access_by_country(self):
        """Tests that internet_access_by_country correctly returns the percentage of a country
        that has internet access. """

        country = "Zambia"
        internet_access = self.data.internet_access_by_country(country)

        result = 26.5

        self.assertEqual(internet_access, result)
    
    def test_internet_access_by_country_edge_case(self):
        """Tests that internet_access_by_country correctly returns the usage statement if
        the user enter an invalid country. """

        country = "Maine"
        internet_access = self.data.internet_access_by_country(country)

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
        
        self.assertEqual(internet_access, message)
    
    def test_tertiary_education_by_country(self):
        """Tests that tertiary_education_by_country correctly returns the percentage of a country
        that has attained tertiary (college) education. """

        country = "Ireland"
        tertiary_education = self.data.tertiary_education_by_country(country)

        result = 45.6

        self.assertEqual(tertiary_education, result)
    
    def test_tertiary_education_by_country_edge_case(self):
        """Tests that tertiary_education_by_country correctly returns the usage statement
        if the user enters an invalid country. """

        country = ""
        tertiary_education = self.data.tertiary_education_by_country(country)

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
        
        self.assertEqual(tertiary_education, message)
    
    def test_population_by_country(self):
        """Tests that population_by_country correctly returns the population of a country. """

        country = "China"
        population = self.data.population_by_country(country)

        result = "1153772544"

        self.assertEqual(population, result) 
    
    def test_population_by_country_edge_case(self):
        """Tests that population_by_country_edge_case correctly returns the usage statement if the user
        enters an invalid country. """

        country = "London"
        population = self.data.population_by_country(country)

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
        
        self.assertEqual(population, message)
    
    def test_employment_by_country(self):
        """Tests that employment_by_country correctly returns the percentage of a country that is employed. """

        country = "Iceland"
        employment = self.data.employment_by_country(country)

        result = 73.3

        self.assertEqual(employment, result)
    
    def test_employment_by_country_edge_case(self):
        """Tests that employment_by_country correctly returns the usage statement if the
        user enters an invalid country. """

        country = "iceland"
        employment = self.data.employment_by_country(country)

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
        
        self.assertEqual(employment, message)
    
    def test_four_stat_summary_by_country(self):
        """Tests that four_stat_summary_by_country correctly returns a formatted string with the
        results of the four statistics of interest for the given country. """

        country = "United States"
        summary = self.data.four_stat_summary_by_country(country)

        result = ['268952128', 94.3, 43.9, 63.1]


        self.assertEqual(summary, result)

    def test_average_age_by_country(self):
        """Tests that average_age_by_country correctly returns the average age of a country. """

        country = "Brazil"
        average_age = self.data.average_age_by_country(country)

        result = 41.2

        self.assertEqual(average_age, result)
    
    def test_average_age_by_country_edge_case(self):
        """Tests that average_age_by_country correctly returns the usage statement if the user enters
        an invalid country. """

        country = "North America"
        average_age = self.data.average_age_by_country(country)

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
        
        
        self.assertEqual(average_age, message)
    
    def test_financial_worry_education_by_country(self):
        """Tests that financial_worry_education_by_country correctly returns the percentage of
        a country that is worried about financing their education. """

        country = "Australia"
        comparison = self.data.financial_worry_education_by_country(country)

        result = 8.8

        self.assertEqual(comparison, result)
    
    def test_financial_worry_education_by_country_edge_case(self):
        """Tests that financial_worry_education_by_country correctly returns the usage statement
        if the user enters an invalid country. """

        country = "Perth"
        comparison = self.data.financial_worry_education_by_country(country)

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
       
        self.assertEqual(comparison, message)
    
    def test_format_age_financial_worry_by_education_summary(self):
        """Tests that format_age_financial_worry_by_education_summary correctly returns the formatted
        results of the age and financial worry comparison functions. """

        country = "Uzbekistan"
        formatted_comparison = self.data.format_age_financial_worry_by_education_summary(country)

        result = "Average age of Uzbekistan: 42.4\nPercentage of people in Uzbekistan who are worried about financing their education: 34.3"
        
        self.assertEqual(formatted_comparison, result)

    """test.dataset.usage_statement() is locked for some reason"""
   
    def test_usage_statement(self):
        """Test identifying whether usage_statement will return correct message when no data is given"""

        result = self.data.usage_statement()

        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
        
        self.assertEqual(result, message)
     
    def test_main_four_stat_summary(self):
        """Tests the main function when the function tag is associated with four_stat_summary. """
        code = subprocess.Popen(["python3", "-u", "cl_code.py", "--function", "four_stat_summary", "--country", "Canada"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()

        result = "Population of Canada: 32009816\nPercentage of Canada that has internet access: 95.2\nPercentage of Canada that has attained tertiary education or higher: 41.5\nPercentage of Canada that is employed: 62.3"

        self.assertEqual(output.strip(), result)

        code.terminate()
    
    def test_main_financial_account(self):
        """Tests the main function when the function tag is associated with financial_account_summary. """

        code = subprocess.Popen(["python3", "-u", "cl_code.py", "--function", "financial_account_comparison", "--country", "Senegal"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()

        result = "Percentage of people in Senegal who have a financial account: 33.9\nPercentage of people worldwide who have a financial account: 65.8"
        
        self.assertEqual(output.strip(), result)

        code.terminate()
    
    def test_main_age_education(self):
        """Tests the main function when the function tag is associated with age_education_worry_comparison. """

        code = subprocess.Popen(["python3", "-u", "cl_code.py", "--function", "age_education_worry_comparison", "--country", "Vietnam"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()

        result = "Average age of Vietnam: 38.0\nPercentage of people in Vietnam who are worried about financing their education: 40.3"
        
        self.assertEqual(output.strip(), result)

        code.terminate()
    
    def test_main_edge_case(self):
        """Tests that the main function will print out the usage statement if the user does not enter a function argument. """
        self.maxDiff = None;
        code = subprocess.Popen(["python3", "-u", "cl_code.py", "--function", "", "--country", "Peru"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, encoding = "utf8")
        output, err = code.communicate()

        message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.data.string_of_countries() + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
        
        self.assertEqual(output.strip(), message)

        code.terminate()

   
if __name__ == '__main__':
    unittest.main()

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    

    
    
    
    
        
        
        
        
        
        
        
        
        
        

    
    
    
    

