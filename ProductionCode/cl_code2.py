import sys
import csv
import argparse

"""USAGE STATEMENTS:
python3 ProductionCode/cl_code.py --internet_access_by_country country_name
python3 ProductionCode/cl_code.py --education_levels_by_country_and_gender country_name"""



def load_data():
    """Loads the data and returns it as a list"""
    
    #global data
    #global header
    
    data = []
    header = {}
    
    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
        column_names = next(reader)
        
        for i, name in enumerate(column_names):
            header[name] = i
            
        for row in reader:
            data.append(row)
            
    return data

def load_header():
    """Loads the column names and returns them as a list"""

    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
        column_names = next(reader)

    return column_names

def get_column_index(column_name):
    """Given a column name, returns the index of the column"""
    
    column_names = load_header()
    idx = column_names.index(column_name)
    
    return idx
    

def filter(by, col, data):
    """Takes a keyword, a column name, and a dataset, and
    returns the portion of the dataset that matches the keyword 
    in the given column as a list"""
    
    new_data = []
    idx = get_column_index(col)
    
    for row in data:
        
        if row[idx] == by:
            new_data.append(row)

    return new_data

def check_country_validity(country, data):
    """Checks if the country that the user entered is in the dataset or if it is an invalid country"""
    is_country_in_data = False
    idx = get_column_index("economy")
    
    for row in data:
        
        if row[idx] == country:
            is_country_in_data = True

    if is_country_in_data == False:
        print("Please enter a valid country. Hint: if the country is multiple words, enclose it in quotes.")
        sys.exit()
    

def get_column(column_name, data):
    """Takes a dataset and a column name, and returns the column as a list""" 
    
    column = []
    idx = get_column_index(column_name)
    
    for row in data:
        column.append(row[idx])
    return column 

def percentage_with_internet_access(country, data):
    """Takes a country name and a dataset, and returns the
    percentage of people that have access to the internet"""
    
    check_country_validity(country, data)
    
    has_internet_access = "1"
    
    country_data = filter(country, "economy", data) 
    
    internet_column = get_column("internetaccess", country_data)
    
    percentage = get_ratio(has_internet_access, internet_column)
    
    return percentage

def get_ratio(key, column):
    """Given a key and a column, returns how often key appeared 
    in the column as a ratio of the length of the column"""
    
    num = column.count(key)
    total = len(column)
    ratio = 0

    ratio = round((num / total) * 100, 1)
    
    return ratio

def get_ratios(column):
    """Given a column, returns a list of counts of items in column
    as a ratio"""
    ratios = []
    
    for item in set(column):
        ratio = get_ratio(item, column)
        ratios.append((int(item), ratio))
        ratios.sort()
        
    return ratios

def get_average_of_column(country, column, data):
    """Returns an average for the given column and country.
    Works for any data is a column in the csv file.
    Inputs: str(country), str(column), data
    Outputs: int(average)"""

    check_country_validity(country, data)

    filtered_data = filter(country, "economy", data)
    filtered_column_data = get_column(column, filtered_data)
    the_averages = calculate_averages(filtered_column_data)

    return the_averages

def calculate_averages(data):

    total = 0
    for i in data:
        if i != '':
            total += int(i)
    length = len(data)

    avg = total / length

    return round(avg, 1)
    
def parse_arguments():
    """Stores the command line arguments in appropriate variables and returns them"""
    function_tag = sys.argv[1]
    country_name = sys.argv[2]

    return function_tag, country_name

def formatted_country_list(data): #test for list of countries
    """Takes in the dataset, and returns a formatted string containing
    the countries in the dataset"""

    string_of_countries = ""

    country_list = get_column("economy", data)
    country_set_unique = unique(country_list)
    country_list_unique = list(country_set_unique)
    country_list_unique.sort()
    
    for country in country_list_unique:       
        string_of_countries += country +'\n'
    
    return string_of_countries

def unique(array):
    """Takes a list and returns all the unique elements in the list"""
    return set(array)

def usage_statement_for_parser(data):
    message = "python3 ProductionCode/cl_code.py --function <function name> --country <country_name>\nFunction options:\ninternet_access_by_country\naverage_age_of_country\n Country options:\nHint: If the country is multiple words long, enclose the name in quotes.\n" + formatted_country_list(data)  # change to cl_code.py later
    
    return message

def main():
    data = load_data()
    parser = argparse.ArgumentParser(usage =usage_statement_for_parser(data))
    parser.add_argument("--function", type = str) #required = False, help = "Please type either internet_access_by_country or average_age_of_country." )
    parser.add_argument("--country", type = str) #required = False, help = "Please enter a valid country. Hint: if the country is multiple words, enclose it in quotes. Here are you options: " + list_of_countries(data))
    arguments = parser.parse_args()

    #if arguments.country is None:
       # print("you didn't enter a country name")

    #if arguments.country not in list_of_countries(data):
        #parser.print_help()

    if arguments.function == "internet_access_by_country":
        percentage_internet_access_by_country = percentage_with_internet_access(arguments.country, data)
        print(str(percentage_internet_access_by_country) + " percent of " + arguments.country + " has internet access.")
    
    elif arguments.function == "average_age_of_country":
        average_age_of_country = get_average_of_column(arguments.country, "age", data)
        print(str(average_age_of_country) + " is the average age of people in " + arguments.country + ".")

    """Loads the data, parses the command line, and prints the results of the specified command line function"""
    
if __name__ == "__main__":
    main()



    
    
    
