import csv
import argparse

class Dataset:
    def __init__(self):
        self.data = []
        self.header = {}
        self.data_subset = []
        
    def load_data(self):
        """Loads the data and returns it as a list
        Output: list [data]"""
         
        with open('Data/world_bank.csv', "r") as file:
            reader = csv.reader(file)
            column_names = next(reader)
            
            for i, col in enumerate(column_names):
                self.header[col] = i
            
            for row in reader:
                self.data.append(row)    
                
    def list_of_countries(self):
        """Returns a list of all countries
        Input: null
        Output: [countries]"""

        country_list = self.get_column("economy", self.data)
        set_country_list = set(country_list)
        country_set_to_list = list(set_country_list)
        country_set_to_list.sort()
    
        return country_set_to_list
    
    def string_of_countries(self):
        """Given a list of countries from the data, returns countries as a string
        Input: list [list_of_countries]
        Output: str(string_of_countries)"""
        
        list_of_countries = self.list_of_countries()

        string_of_countries = ""
        for country in list_of_countries:
            string_of_countries += country +'\n'

        return string_of_countries

    def string_of_countries(list_of_countries):
        """Given a list of countries from the data, returns countries as a string
        Input: list [list_of_countries]
        Output: str(string_of_countries)"""

        string_of_countries = ""
        for country in list_of_countries:
            string_of_countries += country +'\n'

        return string_of_countries

    def check_keyword_validity(self, keyword, keyword_column_title): # Going to be issues
        """ Given a keyword, the column name and data, returns true if the keyword is in the data
        Input: str(keyword), str(keyword_column_title), list[data]
        Output: boolean(is_keyword_in_data)"""
        

        is_keyword_in_data = False
        idx = self.header[keyword_column_title]

        for row in self.data:
            if row[idx] == keyword:
                is_keyword_in_data = True

        return is_keyword_in_data

    def check_column_validity(self, column_title):
        """ Given a column name, returns true if the column is an actual column in the dataset
        Input: str(column_title)
        Output: boolean(is_column_in_data) """
        
        if column_title in self.header.keys():
            return True
        return False

    def get_column(self, column_name, subset):
        """Takes a data subset and a column name, and returns the column as a list
        Input: str(column_name), list [data]
        Output: list [column]""" 
        
        column_validity = self.check_column_validity(column_name)
        if column_validity == True:
            column = []
            idx = self.header[column_name]
        
            for row in subset:
                column.append(row[idx])
            return column 
        else:
            message = "Invalid column name."
            return message

    def filter(self, by, col): # remember this s
        """Takes a keyword, a column name, and a dataset, and
        returns the portion of the dataset that matches the keyword 
        in the given column as a list
        Input: str(by), str(col), list [data]
        Output: list [newData]"""
        
        keyword_validity = self.check_keyword_validity(by, col, self.data)
        column_validity = self.check_column_validity(col)
        isValid = (keyword_validity and column_validity)

        if isValid:
            new_data = []
            idx = self.header[col]
        
            for row in self.data:
            
                if row[idx] == by:
                    new_data.append(row)

            return new_data
        else:
            message = "Invalid keyword or column name."
            return message

    def get_ratio_of_key_in_column(key, column): 
        """Given a key and a column, returns how often key appeared 
        in the column as a ratio of the length of the column
        Inputs: int(key), str(column)
        Output: int(ratio)"""
        
        num = column.count(key)
        total = len(column)
        ratio = 0

        ratio = round((num / total) * 100, 1)
        
        return ratio


    def get_average_of_column(self, country, column):
        """Returns an average for the given column and country.
        Works for any data that is a column in the csv file.
        Inputs: str(country), str(column), list [data]
        Outputs: int(the_averages)"""

        country_validity = self.check_keyword_validity(country, "economy", self.data)

        if country_validity == True:

            filtered_data = filter(country, "economy")
            filtered_column_data = self.get_column(column, filtered_data)
            the_averages = self.calculate_averages(filtered_column_data)

            return the_averages

        else:
            message = self.usage_statement(self.data)
            return message

    def calculate_averages(subset):
        """ Returns the calculated average for the given filtered data.
        Input: list [data]
        Output: int(avg)"""

        total = 0
        for i in subset:
            if i != '':
                total += int(i)
        length = len(subset)
        if length != 0:
            avg = total / length
            return round(avg, 1)
        else:
            return "Cannot calculate the average of no data."

    def has_financial_account_single_country(self, country):
        """Returns the percentage of a country that has a financial account. 
        Input: country (string), data (list)
        Output: percentage of the given country that has a financial account (integer)"""

        country_validity = self.check_keyword_validity(country, "economy")

        if country_validity == True:
            has_account = "1"
            country_data = filter(country, "economy")
            account_column = self.get_column("account_fin", country_data)
            percentage = self.get_ratio_of_key_in_column(has_account, account_column)

            return percentage
        
        else:
            message = self.usage_statement()

            return message

    def has_financial_account_global(self):
        """Returns the percentage of countries worldwide that has a financial account. 
        Input: data (list)
        Output: percentage of people worldwide that have a financial account (integer)"""

        has_account = "1"
        account_column = self.get_column("account_fin", self.data)
        percentage = self.get_ratio_of_key_in_column(has_account, account_column)

        return percentage

    def format_financial_comparison(country, country_result, global_result):
        """Returns the formatted string of the results from the financial account functions. 
        Input: country (string), percentage of people in a given country who have a financial account (integer), 
        percentage of people in countries worldwide who have a financial account (integer)
        Output: formatted results (string)"""

        result = "Percentage of people in " + country + " who have a financial account: " + str(country_result) + "\nPercentage of people worldwide who have a financial account: " + str(global_result)
        
        return result 

    def internet_access_by_country(self, country):
        """Returns the percentage of a country that has internet access. 
        Input: country (string), data (list)
        Output: percentage of the given country that has internet access (integer)"""

        country_validity = self.check_keyword_validity(country, "economy", self.data)

        if country_validity == True:
            has_internet_access = "1"
            country_data = filter(country, "economy") 
            internet_column = self.get_column("internetaccess", country_data)
            percentage = self.get_ratio_of_key_in_column(has_internet_access, internet_column)

            return percentage
        
        else:
            message = self.usage_statement()

            return message
        
    def tertiary_education_by_country(self, country):
        """Returns the percentage of a country that has attained tertiary (college) education. 
        Input: country (string), data (list)
        Output: percentage of the given country that has attainted tertiary education (integer)"""

        country_validity = self.check_keyword_validity(country, "economy", self.data)

        if country_validity == True:
            tertiary_or_higher = "3"
            country_data = filter(country, "economy")
            urbanicity_column = self.get_column("educ", country_data)
            percentage = self.get_ratio_of_key_in_column(tertiary_or_higher, urbanicity_column)

            return percentage
        
        else:
            message = self.usage_statement()

            return message

    def population_by_country(self, country):
        """Returns the population of a country. 
        Input: country (string)
        Output: population of the given country (integer)"""

        country_validity = self.check_keyword_validity(country, "economy", self.data)

        if country_validity == True:
            population_column_index = self.get_column_index("pop_adult")
            country_data = filter(country, "economy")
            population = country_data[0][population_column_index]

            return population
        
        else:
            message = self.usage_statement()

            return message

    def employment_by_country(self, country):
        """Returns the percentage of a country that is employed. 
        Input: country (string), data (list)
        Output: percentage of the given country that is employed (integer)"""

        country_validity = self.check_keyword_validity(country, "economy", self.data)

        if country_validity == True:
            employed = "1"
            country_data = filter(country, "economy")
            employment_column = self.get_column("emp_in", country_data)
            percentage = self.get_ratio_of_key_in_column(employed, employment_column)

            return percentage
        
        else:
            message = self.usage_statement()

            return message

    def four_stat_summary_by_country(self, country):
        """Returns a summary of four interesting statistics for a country: percentage with internet access,
        percentage that has attained tertiary education, population, and percentage that is employed. 
        Input: country (string), data (list)
        Output: Formatted results (string)"""

        internet_access_stat = self.internet_access_by_country(country)
        education_stat = self.tertiary_education_by_country(country)
        population_stat = self.population_by_country(country)
        employment_stat = self.employment_by_country(country)

        results_message = "Percentage of " + country + " with internet access: " + str(internet_access_stat) + "\nPercentage of " + country + " that has attained tertiary education or higher: " + str(education_stat) + "\nPopulation of " + country + ": " + str(population_stat) + "\nPercentage of " + country + " that is employed: " + str(employment_stat)
        
        return results_message

    def average_age_by_country(self, country):
        """Returns the average age of a country. 
        Input: country (string), data (list)
        Output: average age of the given country (integer)"""

        country_validity = self.check_keyword_validity(country, "economy")

        if country_validity == True:
            average_age_of_country = self.get_average_of_column(country, "age")

            return average_age_of_country
        
        else:
            message = self.usage_statement()

            return message

    def financial_worry_education_by_country(self, country):
        """Returns the percentage of a country that is worried about financing their education.
        Input: country (string), data (list)
        Output: percentage of the given country that is worried about financing their education. """

        country_validity = self.check_keyword_validity(country, "economy")

        if country_validity:
            very_worried_about_finances_of_education = "1"
            somewhat_worried_about_finances_of_education = "2"

            country_data = filter(country, "economy")
            education_finances_column = self.get_column("fin44d", country_data)
            very_worried_percentage = self.get_ratio_of_key_in_column(very_worried_about_finances_of_education, education_finances_column)
            somewhat_worried_percentage = self.get_ratio_of_key_in_column(somewhat_worried_about_finances_of_education, education_finances_column)

            return very_worried_percentage + somewhat_worried_percentage
        
        else:
            message = self.usage_statement()
            return message

    def format_age_financial_worry_by_education_summary(self, country):
        """Returns the formatted results of the average age of a country and the percentage of that country 
        that is worried about financing their education.
        Input: country (string), data (list)
        Output: formatted results for the age and financial worry stats for the given country (string)"""

        average_age = self.average_age_by_country(country)
        financial_worry = self.financial_worry_education_by_country(country)
        results = "Average age of " + country + ": " + str(average_age) + "\nPercentage of people in " + country + " who are worried about financing their education: " + str(financial_worry)
        
        return results

    def usage_statement(self):
        """ Returns the usage statement
        Output: str(message) """
        #country_list = self.list_of_countries()
        message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.string_of_countries() + "To view this information at any time, type 'python3 ProductionCode/cl_code.py -h' in the command line."
    
        return message

def main():
    """Loads the data, parses the command line, and prints the results of the specificed command line function.
    Output: four_stat_summary result (string), financial_account_comparison result (string), or
    age_education_worry_comparison result (string)"""

    data = Dataset()
    data.load_data()
    country_list = data.list_of_countries()

    parser = argparse.ArgumentParser(usage = data.usage_statement())
    parser.add_argument("--function", type = str, help = "Usage: python3 ProductionCode/cl_code.py --function <function_name> \
                        --country <country_name>\nFunction options:\nfour_stat_summary, financial_account_comparison, age_education_worry_comparison") 
    parser.add_argument("--country", type = str, help = "Country options:\nHint: If the country is multiple words long, \
                        enclose the name in quotes.\n" + data.string_of_countries())
    arguments = parser.parse_args()

    country_validity = data.check_keyword_validity(arguments.country, "economy")

    if country_validity == True:

        if arguments.function == "four_stat_summary":
            four_main_stats_of_interest = data.four_stat_summary_by_country(arguments.country, data)
            print(four_main_stats_of_interest)
    
        elif arguments.function == "financial_account_comparison":
            financial_account_by_country = data.has_financial_account_single_country(arguments.country, data)
            financial_account_global = data.has_financial_account_global(data)
            results = data.format_financial_comparison(arguments.country, financial_account_by_country, financial_account_global)
            print(results)
    
        elif arguments.function == "age_education_worry_comparison":
            results = data.format_age_financial_worry_by_education_summary(arguments.country, data)
            print(results)

        else:
            usage_statement_message = data.usage_statement()
            print(usage_statement_message)
    
    else:
        usage_statement_message = data.usage_statement()
        print(usage_statement_message)

    
if __name__ == "__main__":
    main()



    
    
    
