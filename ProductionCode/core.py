import csv, psycopg2
import ProductionCode.psqlConfig as config #change to import ProductionCode.psqlConfig as config for app to work
# check that command line portion still works

#TODO tonight: 
# - delete commented out code
# - implement check country validity everywhere it needs to go
# - add updated/appropriate comments
# - update the query in check country validity to make the function shorter
# - change function names to "get" for accesssors?
# - class work?? seems we can do this later?
# - deal with Afghanistan??



class Dataset:
    
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        try:
            connection = psycopg2.connect(database = config.database, user = config.user, password = config.password, host = "localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
                        
    def list_of_countries(self):
        """Returns a list of all countries
        Input: null
        Output: [countries]"""

        cursor = self.connection.cursor()
        cursor.execute("SELECT country FROM countries")
        list_of_all_countries = cursor.fetchall()

        return list_of_all_countries


    def string_of_countries(self): 
        """Given a list of countries from the data, returns countries as a string
        Input: list [list_of_countries]
        Output: str(string_of_countries)"""

        list_of_all_countries = self.list_of_countries()
        
        string_of_countries = ""
        for country_tuple in list_of_all_countries:
            country = country_tuple[0]
            string_of_countries += country +'\n'

        return string_of_countries

    def check_country_validity(self, keyword):
        """ Given a keyword, the column name and data, returns true if the keyword is in the data
        Input: str(keyword), str(keyword_column_title), list[data]
        Output: boolean(is_keyword_in_data)"""

        all_countries = self.list_of_countries()

        for country_in_data in all_countries:
            current_country = country_in_data[0]
            if keyword.strip() == current_country.strip():
                return True

        return False
       

    def get_column(self, column_name, subset):
        """Takes a data subset and a column name, and returns the column as a list
        Input: str(column_name), list [data]
        Output: list [column]""" 
        column_validity = self.check_column_validity(column_name)
        if column_validity == True:
            all_column =  "SELECT" + column_name + "FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.employment_status <> '';"
            cursor = self.connection.cursor()
            column_data = cursor.fetchall()
            return column_data
        else:
            message = "Invalid column name."
            return message


    def has_financial_account_single_country(self, country):
        """Returns the percentage of a country that has a financial account. 
        Input: country (string), data (list)
        Output: percentage of the given country that has a financial account (integer)"""

        country_validity = self.check_country_validity(country)
        if country_validity == True:

            total_financial_account_status_responses_by_country = "SELECT COUNT(financial_account_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.financial_account_status <> '';"
            has_financial_account_by_country = "SELECT COUNT(financial_account_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.financial_account_status = '1';"

            cursor = self.connection.cursor()

            cursor.execute(total_financial_account_status_responses_by_country, (country.strip(),))
            total_financial_account_status_by_country_responses = cursor.fetchall()

            cursor.execute(has_financial_account_by_country, (country.strip(),))
            financial_account_status_by_country_result = cursor.fetchall()

            percentage = (financial_account_status_by_country_result[0][0] / total_financial_account_status_by_country_responses[0][0]) * 100

            return round(percentage, 1)

        else:
            return "Attempted to run a query on an invalid country. "


    def has_financial_account_global(self): 
        """Returns the percentage of countries worldwide that has a financial account. 
        Input: data (list)
        Output: percentage of people worldwide that have a financial account (integer)"""

        total_financial_account_status_responses_global = "SELECT COUNT(financial_account_status) FROM poll_results;"
        financial_account_status_global = "SELECT COUNT(financial_account_status) FROM poll_results WHERE poll_results.financial_account_status = '1';"

        cursor = self.connection.cursor()

        cursor.execute(total_financial_account_status_responses_global)
        total_financial_account_status_global_response = cursor.fetchall()

        cursor.execute(financial_account_status_global)
        financial_account_status_global_result = cursor.fetchall()

        percentage = (financial_account_status_global_result[0][0] / total_financial_account_status_global_response[0][0]) * 100

        return round(percentage, 1)

    def format_financial_comparison(self, country):
        """Returns the formatted string of the results from the financial account functions. 
        Input: country (string), percentage of people in a given country who have a financial account (integer), 
        percentage of people in countries worldwide who have a financial account (integer)
        Output: formatted results (string)"""

        country_result = self.has_financial_account_single_country(country)
        global_result = self.has_financial_account_global()

        result = "Percentage of people in " + country + " who have a financial account: " + str(country_result) + "\nPercentage of people worldwide who have a financial account: " + str(global_result)
        
        return result 

    def internet_access_by_country(self, country): 
        """Returns the percentage of a country that has internet access. 
        Input: country (string), data (list)
        Output: percentage of the given country that has internet access (integer)"""

        country_validity = self.check_country_validity(country)
        if country_validity == True:

            total_internet_responses_by_country = "SELECT COUNT(internet_access) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.internet_access <> '';"
            has_internet_responses_by_country = "SELECT COUNT(internet_access) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.internet_access = '1';"
        
            cursor = self.connection.cursor()

            cursor.execute(total_internet_responses_by_country, (country.strip(),))
            total_internet_responses_by_country_result = cursor.fetchall()

            cursor.execute(has_internet_responses_by_country, (country.strip(),))
            has_internet_responses_by_country_result = cursor.fetchall()

            percentage = (has_internet_responses_by_country_result[0][0] / total_internet_responses_by_country_result[0][0]) * 100

            return round(percentage, 1)

        else:
            return "Attempted to run a query on an invalid country. "

        
    def tertiary_education_by_country(self, country):
        """Returns the percentage of a country that has attained tertiary (college) education. 
        Input: country (string), data (list)
        Output: percentage of the given country that has attainted tertiary education (integer)"""

        country_validity = self.check_country_validity(country)
        if country_validity == True:

            total_education_responses_by_country = "SELECT COUNT(education_level) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.education_level <> '';"
            attained_tertiary_education_by_country = "SELECT COUNT(education_level) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.education_level = '3';"

            cursor = self.connection.cursor()

            cursor.execute(total_education_responses_by_country, (country.strip(),))
            total_education_responses_by_country_result = cursor.fetchall()

            cursor.execute(attained_tertiary_education_by_country, (country.strip(),))
            attained_tertiary_education_by_country_result = cursor.fetchall()

            percentage = (attained_tertiary_education_by_country_result[0][0] / total_education_responses_by_country_result[0][0]) * 100

            return round(percentage, 1)

        else:
            return "Attempted to run a query on an invalid country. "


    def population_by_country(self, country):
        """Returns the population of a country. 
        Input: country (string)
        Output: population of the given country (integer)"""

        country_validity = self.check_country_validity(country)
        if country_validity == True:

            population_by_country = "SELECT adult_population FROM countries WHERE country = %s;"

            cursor = self.connection.cursor()

            cursor.execute(population_by_country, (country.strip(),))
            population_by_country_result = cursor.fetchall()

            return population_by_country_result[0][0]
        
        else:
            return "Attempted to run a query on an invalid country. "


    def employment_by_country(self, country):
        """Returns the percentage of a country that is employed. 
        Input: country (string), data (list)
        Output: percentage of the given country that is employed (integer)"""

        country_validity = self.check_country_validity(country)
        if country_validity == True:

            total_employment_responses_by_country = "SELECT COUNT(employment_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.employment_status <> '';"
            employed_persons_by_country = "SELECT COUNT(employment_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.employment_status = '1';"

            cursor = self.connection.cursor()

            cursor.execute(total_employment_responses_by_country, (country.strip(),))
            total_employment_responses_by_country_result = cursor.fetchall()

            cursor.execute(employed_persons_by_country, (country.strip(),))
            employed_persons_by_country_result = cursor.fetchall()

            percentage = (employed_persons_by_country_result[0][0] / total_employment_responses_by_country_result[0][0]) * 100

            return round(percentage, 1)

        else:
            return "Attempted to run a query on an invalid country. "


    def four_stat_summary_by_country(self, country):
        """Returns a summary of four interesting statistics for a country: percentage with internet access,
        percentage that has attained tertiary education, population, and percentage that is employed. 
        Input: country (string), data (list)
        Output: Results (list)"""
    
        population_stat = self.population_by_country(country)
        internet_access_stat = self.internet_access_by_country(country)
        education_stat = self.tertiary_education_by_country(country)
        employment_stat = self.employment_by_country(country)

        results = [population_stat, internet_access_stat, education_stat, employment_stat]
        
        return results
    
    def format_four_stat_summary_by_country(self, country):
        """Returns the formatted results of the four intersting statistic summary for
        a given country. 
        Input: country (string)
        Output: formatted results (string)"""
        summary = self.four_stat_summary_by_country(country)

        population = summary[0]
        internet = summary[1]
        education = summary[2]
        employment = summary[3]

        message = "Population of " + country + ": " + str(population) + "\nPercentage of " + country + " that has internet access: " + str(internet) + "\nPercentage of " + country + " that has attained tertiary education or higher: " + str(education) + "\nPercentage of " + country + " that is employed: " + str(employment)

        return message
    
    def cast_value_to_integer(self, value):
        """NEEDS DOCSTRING"""
        cast_the_value = "SELECT CAST(%s AS int)"

        cursor = self.connection.cursor()
        cursor.execute(cast_the_value, (value,))
        result = cursor.fetchall()

        return result[0][0]
    
    def average_age_by_country(self, country):
        """Returns the average age of a country. 
        Input: country (string), data (list)
        Output: average age of the given country (integer)"""

        country_validity = self.check_country_validity(country)
        if country_validity == True:

            average_age_by_country = "SELECT AVG(age) FROM poll_results INNER JOIN countries on poll_results.country_id = countries.id WHERE countries.country = %s;"
            
            cursor = self.connection.cursor()
            cursor.execute(average_age_by_country, (country.strip(),))
            result = cursor.fetchall()

            cast_result_to_type_int = self.cast_value_to_integer(result[0])
        
            return cast_result_to_type_int

        else:
            return "Attempted to run a query on an invalid country. "


    def financial_worry_education_by_country(self, country):
        """Returns the percentage of a country that is worried about financing their education.
        Input: country (string), data (list)
        Output: percentage of the given country that is worried about financing their education. """

        country_validity = self.check_country_validity(country)
        if country_validity == True:
        
            total_financial_worry_responses_by_country = "SELECT COUNT(worry_about_financing_education) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.worry_about_financing_education <> '';"
            is_worried_about_financing_education_by_country = "SELECT COUNT(worry_about_financing_education) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND (poll_results.worry_about_financing_education = '1' OR poll_results.worry_about_financing_education = '2');"

            cursor = self.connection.cursor()

            cursor.execute(total_financial_worry_responses_by_country, (country.strip(),))
            total_financial_worry_responses_by_country_result = cursor.fetchall()


            cursor.execute(is_worried_about_financing_education_by_country, (country.strip(),))
            is_worried_about_financing_education_by_country_result = cursor.fetchall()

            percentage = (is_worried_about_financing_education_by_country_result[0][0] / total_financial_worry_responses_by_country_result[0][0]) * 100

            return round(percentage, 1)
        
        else:
            return "Attempted to run a query on an invalid country. "


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
        message = "python3 cl_code.py --function <function_name> --country <country_name> \
            \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
            \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
    
        return message


