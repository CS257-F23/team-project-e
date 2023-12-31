import csv, psycopg2
import ProductionCode.psqlConfig as config


class Dataset:


   def __init__(self):
       """Creates a connection variable that represents the connection to the database. """
       self.connection = self.connect()


   def connect(self):
       """Connects to the database.
       Input: None
       Returns: connection object"""


       try:
           connection = psycopg2.connect(database = config.database, user = config.user, password = config.password, host = "localhost")
       except Exception as e:
           print("Connection error: ", e)
           exit()
       return connection
                      
   def get_list_of_countries(self):
       """Returns a list of of all the countries in the data set.
       Input: None
       Returns: all the countries in the data set (list)"""


       cursor = self.connection.cursor()
       cursor.execute("SELECT country FROM countries")
       list_of_all_countries = cursor.fetchall()


       return list_of_all_countries




   def get_string_of_countries(self):
       """Given a list of countries from the data, returns all the countries as a string.
       Input: None
       Returns: all the countries in the data set (string)"""


       list_of_all_countries = self.get_list_of_countries()
      
       string_of_countries = ""
       for country_tuple in list_of_all_countries:
           country = country_tuple[0]
           string_of_countries += country +'\n'


       return string_of_countries


   def get_country_validity(self, keyword):
       """Given a country, checks if the country is in the data set.
       Input: country (string)
       Returns: if the country is in the data set (boolean)"""


       all_countries = self.get_list_of_countries()


       for country_in_data in all_countries:
           current_country = country_in_data[0]
           if keyword.strip() == current_country.strip():
               return True


       return False


   def get_financial_account_status_single_country_financial_helper(self, country):
       """Helper function for get_financial_account_status_single_country
           Input: country(string)
           Output: Selected data"""




       has_financial_account_by_country = "SELECT COUNT(financial_account_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.financial_account_status = 1;"


       cursor = self.connection.cursor()


       cursor.execute(has_financial_account_by_country, (country.strip(),))
       financial_account_status_by_country_result = cursor.fetchall()
      
       return financial_account_status_by_country_result




   def get_financial_account_status_single_country_total_account_helper(self, country):
       """Helper function for get_financial_account_status_single_country
           Input: country(string)
           Output: Selected data"""


       total_financial_account_status_responses_by_country = "SELECT COUNT(financial_account_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.financial_account_status IS NOT NULL;"
      
       cursor = self.connection.cursor()


       cursor.execute(total_financial_account_status_responses_by_country, (country.strip(),))
       total_financial_account_status_by_country_responses = cursor.fetchall()


       return total_financial_account_status_by_country_responses




   def get_financial_account_status_single_country(self, country):
       """Returns the percentage of a country that has a financial account.
           Input: country (string)
           Returns: percentage of the given country that has a financial account (integer)"""


       if self.get_country_validity(country):


           selected_total_account_data = self.get_financial_account_status_single_country_total_account_helper(country)
           selected_account_data = self.get_financial_account_status_single_country_financial_helper(country)


           percentage = (selected_account_data[0][0] / selected_total_account_data[0][0]) * 100
          
           return round(percentage, 1)


       else:
           return "Attempted to run a query on an invalid country. "


   def get_financial_account_count_helper(self):
       """Helper function for get_financial_account_status_global
       Input: """


       total_financial_account_status_responses_global = "SELECT COUNT(financial_account_status) FROM poll_results;"


       cursor = self.connection.cursor()


       cursor.execute(total_financial_account_status_responses_global)
       total_financial_account_status_global_response = cursor.fetchall()


       return total_financial_account_status_global_response


      


   def get_financial_account_data_helper(self):
       """Helper function for get_financial_account_status_global
       Input: Null
       Output: financial account global response"""
       financial_account_status_global = "SELECT COUNT(financial_account_status) FROM poll_results WHERE poll_results.financial_account_status = 1;"


       cursor = self.connection.cursor()


       cursor.execute(financial_account_status_global)
       financial_account_status_global_result = cursor.fetchall()


       return financial_account_status_global_result




   def get_financial_account_status_global(self):
       """Returns the percentage of countries worldwide that has a financial account.
       Input: None
       Returns: percentage of people worldwide that have a financial account (integer)"""


       financial_account_status_global_result = self.get_financial_account_data_helper()
       total_financial_account_status_global_response = self.get_financial_account_count_helper()


       percentage = (financial_account_status_global_result[0][0] / total_financial_account_status_global_response[0][0]) * 100


       return round(percentage, 1)


   def get_formatted_financial_comparison(self, country):
       """Returns the formatted string of the results from the financial account functions.
       Input: country (string), percentage of people in a given country who have a financial account (integer),
       percentage of people in countries worldwide who have a financial account (integer)
       Returns: formatted results (string)"""


       if self.get_country_validity(country):


           country_result = self.get_financial_account_status_single_country(country)
           global_result = self.get_financial_account_status_global()


           result = "Percentage of people in " + country + " who have a financial account: " + str(country_result) + "\nPercentage of people worldwide who have a financial account: " + str(global_result)
          
           return result


       else:
           return "Attempted to run a query on an invalid country. "


   def get_internet_access_total_reponse_helper(self, country):
       """get_internet_access_by_country helper function
       input: country(string)
       Output: count of total internet access"""


       total_internet_responses_by_country = "SELECT COUNT(internet_access) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.internet_access IS NOT NULL;"


       cursor = self.connection.cursor()


       cursor.execute(total_internet_responses_by_country, (country.strip(),))
       total_internet_responses_by_country_result = cursor.fetchall()


       return total_internet_responses_by_country_result


   def get_internet_access_has_internet_reponse_helper(self, country):
       """get_internet_access_by_country helper function
       input: country(string)
       Output: count of people with internet access"""


       has_internet_responses_by_country = "SELECT COUNT(internet_access) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.internet_access = 1;"
      
       cursor = self.connection.cursor()


       cursor.execute(has_internet_responses_by_country, (country.strip(),))
       has_internet_responses_by_country_result = cursor.fetchall()


       return has_internet_responses_by_country_result




   def get_internet_access_by_country(self, country):
       """Returns the percentage of a country that has internet access.
       Input: country (string)
       Returns: percentage of the given country that has internet access (integer)"""


       if self.get_country_validity(country):


           has_internet_responses_by_country_result = self.get_internet_access_has_internet_reponse_helper(country)
           total_internet_responses_by_country_result = self.get_internet_access_total_reponse_helper(country)
           print(has_internet_responses_by_country_result)
       


           percentage = (has_internet_responses_by_country_result[0][0] / total_internet_responses_by_country_result[0][0]) * 100


           return round(percentage, 1)


       else:
           return "Attempted to run a query on an invalid country. "


   def get_total_education_by_country_helper(self, country):
       """Helper function for get_tertiary_education_by_country
       Input: country (string)
       Returns: count of total education"""
          
       total_education_responses_by_country = "SELECT COUNT(education_level) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.education_level IS NOT NULL;"


       cursor = self.connection.cursor()


       cursor.execute(total_education_responses_by_country, (country.strip(),))
       total_education_responses_by_country_result = cursor.fetchall()


       return total_education_responses_by_country_result


   def get_tertiary_education_by_country_helper(self, country):
       """Helper function for get_tertiary_education_by_country
       Input: country (string)
       Returns: count of tertiary education in country"""


       attained_tertiary_education_by_country = "SELECT COUNT(education_level) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.education_level = 3;"


       cursor = self.connection.cursor()


       cursor.execute(attained_tertiary_education_by_country, (country.strip(),))
       attained_tertiary_education_by_country_result = cursor.fetchall()


       return attained_tertiary_education_by_country_result


      
   def get_tertiary_education_by_country(self, country):
       """Returns the percentage of a country that has attained tertiary (college) education.
       Input: country (string)
       Returns: percentage of the given country that has attainted tertiary education (integer)"""


       if self.get_country_validity(country):


           attained_tertiary_education_by_country_result = self.get_tertiary_education_by_country_helper(country)
           total_education_responses_by_country_result = self.get_total_education_by_country_helper(country)


           percentage = (attained_tertiary_education_by_country_result[0][0] / total_education_responses_by_country_result[0][0]) * 100


           return round(percentage, 1)


       else:
           return "Attempted to run a query on an invalid country. "




   def get_population_by_country(self, country):
       """Returns the population of a country.
       Input: country (string)
       Returns: population of the given country (integer)"""


       if self.get_country_validity(country):


           population_by_country = "SELECT adult_population FROM countries WHERE country = %s;"


           cursor = self.connection.cursor()


           cursor.execute(population_by_country, (country.strip(),))
           population_by_country_result = cursor.fetchall()




           return round(population_by_country_result[0][0])
      
       else:
           return "Attempted to run a query on an invalid country. "


   def total_employment_by_country_helper(self, country):
       """Helper function for get_employment_by_country
       Input: country (string)
       Output: total number of people having employment stats gotten in the country"""


       total_employment_responses_by_country = "SELECT COUNT(employment_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.employment_status IS NOT NULL;"


       cursor = self.connection.cursor()


       cursor.execute(total_employment_responses_by_country, (country.strip(),))
       total_employment_responses_by_country_result = cursor.fetchall()


       return total_employment_responses_by_country_result


   def employment_by_country_helper(self, country):
       """Helper function for get_employment_by_country
       Input: country (string)
       Output: number of people with employment gotten in the country"""


       employed_persons_by_country = "SELECT COUNT(employment_status) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.employment_status = 1;"


       cursor = self.connection.cursor()


       cursor.execute(employed_persons_by_country, (country.strip(),))
       employed_persons_by_country_result = cursor.fetchall()


       return employed_persons_by_country_result


   def get_employment_by_country(self, country): #TODO Break Up
       """Returns the percentage of a country that is employed.
       Input: country (string)
       Returns: percentage of the given country that is employed (integer)"""


       if self.get_country_validity(country):


           employed_persons_by_country_result = self.employment_by_country_helper(country)
           total_employment_responses_by_country_result = self.total_employment_by_country_helper(country)
          
           percentage = (employed_persons_by_country_result[0][0] / total_employment_responses_by_country_result[0][0]) * 100


           return round(percentage, 1)


       else:
           return "Attempted to run a query on an invalid country. "




   def get_four_stat_summary_by_country(self, country):
       """Returns a summary of four interesting statistics for a country: percentage with internet access,
       percentage that has attained tertiary education, population, and percentage that is employed.
       Input: country (string)
       Returns: results of those four statistics (list)"""
  
       population_stat = self.get_population_by_country(country)
       internet_access_stat = self.get_internet_access_by_country(country)
       education_stat = self.get_tertiary_education_by_country(country)
       employment_stat = self.get_employment_by_country(country)


       results = [population_stat, internet_access_stat, education_stat, employment_stat]
      
       return results
  
   def get_formatted_four_stat_summary_by_country(self, country):
       """Returns the formatted results of the four intersting statistic summary for
       a given country.
       Input: country (string)
       Returns: formatted results (string)"""


       if self.get_country_validity(country):


           summary = self.get_four_stat_summary_by_country(country)


           population = summary[0]
           internet = summary[1]
           education = summary[2]
           employment = summary[3]


           message = "Population of " + country + ": " + str(population) + "\nPercentage of " + country + " that has internet access: " + str(internet) + "\nPercentage of " + country + " that has attained tertiary education or higher: " + str(education) + "\nPercentage of " + country + " that is employed: " + str(employment)


           return message
      
       else:
           return "Attempted to run a query on an invalid country. "
   
   def get_average_age_by_country(self, country):
       """Returns the average age of a country.
       Input: country (string)
       Returns: average age of the given country (integer)"""


       if self.get_country_validity(country):


           average_age_by_country = "SELECT AVG(age) FROM poll_results INNER JOIN countries on poll_results.country_id = countries.id WHERE countries.country = %s;"
          
           cursor = self.connection.cursor()
           cursor.execute(average_age_by_country, (country.strip(),))
           result = cursor.fetchall()
      
           return round(result[0][0])


       else:
           return "Attempted to run a query on an invalid country. "


   def get_financial_worry_education_by_country_total_helper(self, country):
       """Helper function for get_financial_worry_education_by_country
       Input: country (string)
       Output: total count of people who had data collected"""


       total_financial_worry_responses_by_country = "SELECT COUNT(worry_about_financing_education) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND poll_results.worry_about_financing_education IS NOT NULL;"


       cursor = self.connection.cursor()


       cursor.execute(total_financial_worry_responses_by_country, (country.strip(),))
       total_financial_worry_responses_by_country_result = cursor.fetchall()


       return total_financial_worry_responses_by_country_result


   def get_financial_worry_education_by_country_helper(self, country):
       """Helper function for get_financial_worry_education_by_country
       Input: country (string)
       Output: specific financial worry count of people who had data collected"""


       is_worried_about_financing_education_by_country = "SELECT COUNT(worry_about_financing_education) FROM poll_results INNER JOIN countries ON poll_results.country_id = countries.id WHERE countries.country = %s AND (poll_results.worry_about_financing_education = 1 OR poll_results.worry_about_financing_education = 2);"


       cursor = self.connection.cursor()


       cursor.execute(is_worried_about_financing_education_by_country, (country.strip(),))
       is_worried_about_financing_education_by_country_result = cursor.fetchall()
      
       return is_worried_about_financing_education_by_country_result


   def get_financial_worry_education_by_country(self, country):
       """Returns the percentage of a country that is worried about financing their education.
       Input: country (string)
       Returns: percentage of the given country that is worried about financing their education (integer)"""


       if self.get_country_validity(country):


           is_worried_about_financing_education_by_country_result = self.get_financial_worry_education_by_country_helper(country)
           total_financial_worry_responses_by_country_result = self.get_financial_worry_education_by_country_total_helper(country)


           percentage = (is_worried_about_financing_education_by_country_result[0][0] / total_financial_worry_responses_by_country_result[0][0]) * 100


           return round(percentage, 1)
      
       else:
           return "Attempted to run a query on an invalid country. "




   def get_formatted_age_financial_worry_by_education_summary(self, country):
       """Returns the formatted results of the average age of a country and the percentage of that country
       that is worried about financing their education.
       Input: country (string)
       Returns: formatted results (string)"""


       if self.get_country_validity(country):


           average_age = self.get_average_age_by_country(country)
           financial_worry = self.get_financial_worry_education_by_country(country)
           results = "Average age of " + country + ": " + str(average_age) + "\nPercentage of people in " + country + " who are worried about financing their education: " + str(financial_worry)
          
           return results
      
       else:
           return "Attempted to run a query on an invalid country. "


   def get_usage_statement(self):
       """Returns the usage statement.
       Input: None
       Output: usage message (string)"""


       message = "python3 cl_code.py --function <function_name> --country <country_name> \
           \nFunction options:\nfour_stat_summary\nfinancial_account_comparison\nage_education_worry_comparison\nCountry options: \
           \nHint: If the country is multiple words long, enclose the name in quotes.\n" + self.get_string_of_countries() + "To view this information at any time, type 'python3 cl_code.py -h' in the command line."
  
       return message