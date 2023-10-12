import csv
import argparse

"""Usage statement:
python3 ProductionCode/cl_code.py --function <function_name> --country <country_name>
"""

def load_data():
    """Loads the data and returns it as a list
    Output: list [data]"""
    
    data = []
    
    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
            
        for row in reader:
            data.append(row)
            
    return data

def load_header():
    """Loads the column names and returns them as a list
    Output: list[column_names]"""

    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
        column_names = next(reader)

    return column_names

def list_of_countries(data):
    """Returns a list of all countries
    Input: null
    Output: [countries]"""

    country_list = get_column("economy", data)
    set_country_list = set(country_list)
    country_set_to_list = list(set_country_list)
    country_set_to_list.sort()
    
    return country_set_to_list

def string_of_countries(list_of_countries):
    """Given a list of countries from the data, returns countries as a string
    Input: list [list_of_countries]
    Output: str(string_of_countries)"""

    string_of_countries = ""
    for country in list_of_countries:
        string_of_countries += country +'\n'

    return string_of_countries

def check_keyword_validity(keyword, keyword_column_title, data):
    """ Given a keyword, the column name and data, returns true if the keyword is in the data
    Input: str(keyword), str(keyword_column_title), list[data]
    Output: boolean(is_keyword_in_data)"""

    is_keyword_in_data = False
    idx = get_column_index(keyword_column_title)

    for row in data:
        if row[idx] == keyword:
            is_keyword_in_data = True

    return is_keyword_in_data

def check_column_validity(column_title):
    """ Given a column name, returns true if the column is an actual column in the dataset
    Input: str(column_title)
    Output: boolean(is_column_in_data) """

    is_column_in_data = False
    header = load_header()

    for column in header:
        if column == column_title:
            is_column_in_data = True
    
    return is_column_in_data

def get_column_index(column_name):
    """Given a column name, returns the index of the column
    Input: str(column_name)
    Output: int(idx)"""
 
    column_validity = check_column_validity(column_name)

    if column_validity == True:
        column_names = load_header()
        idx = column_names.index(column_name)
    
        return idx
    else:
        message = "Invalid column name."
        return message


def get_column(column_name, data):
    """Takes a dataset and a column name, and returns the column as a list
    Input: str(column_name), list [data]
    Output: list [column]""" 
    
    column_validity = check_column_validity(column_name)
    if column_validity == True:
        column = []
        idx = get_column_index(column_name)
    
        for row in data:
            column.append(row[idx])
        return column 
    else:
        message = "Invalid column name."
        return message

def filter(by, col, data):
    """Takes a keyword, a column name, and a dataset, and
    returns the portion of the dataset that matches the keyword 
    in the given column as a list
    Input: str(by), str(col), list [data]
    Output: list [newData]"""
    
    keyword_validity = check_keyword_validity(by, col, data)
    column_validity = check_column_validity(col)

    if keyword_validity == True and column_validity == True:
        new_data = []
        idx = get_column_index(col)
    
        for row in data:
        
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
    #else:Morr
        #message = "Invalid keyword."
        #return message

def get_average_of_column(country, column, data):
    """Returns an average for the given column and country.
    Works for any data is a column in the csv file.
    Inputs: str(country), str(column), list [data]
    Outputs: int(the_averages)"""

    country_validity = check_keyword_validity(country, "economy", data)

    if country_validity == True:

        filtered_data = filter(country, "economy", data)
        filtered_column_data = get_column(column, filtered_data)
        the_averages = calculate_averages(filtered_column_data)

        return the_averages

    else:
        message = usage_statement(data)
        return message

def calculate_averages(data):
    """ Returns the calculated average for the given filtered data.
    Input: list [data]
    Output: int(avg)"""
    total = 0
    for i in data:
        if i != '':
            total += int(i)
    length = len(data)
    if length != 0:
        avg = total / length
        return round(avg, 1)
    else:
        return "Cannot calculate the average of no data."

def percentage_with_internet_access(country, data):
    """Takes a country name and a dataset, and returns the
    percentage of people that have access to the internet
    Input: str(country), list [data]
    Output: int(percentage)"""
    
    country_validity = check_keyword_validity(country, "economy", data)

    if country_validity == True:
    
        has_internet_access = "1"
    
        country_data = filter(country, "economy", data) 
    
        internet_column = get_column("internetaccess", country_data)
    
        percentage = get_ratio_of_key_in_column(has_internet_access, internet_column)
    
        return percentage
    else:
        message = usage_statement(data)
        return message


def usage_statement(data):
    """ Returns the usage statement
        Output: str(message) """
    country_list = list_of_countries(data)
    message = "python3 ProductionCode/cl_code.py --function <function_name> --country <country_name> \
        \nFunction options:\ninternet_access_by_country\naverage_age_of_country\nCountry options: \
        \nHint: If the country is multiple words long, enclose the name in quotes.\n" + string_of_countries(country_list) + "To view this information at any time, type '-h' in the command line."
    
    return message

def main():
    """Loads the data, parses the command line, and prints the results of the specificed command line function.
    Output: str(internet_result) or str(age_result)"""
    data = load_data()
    ratios = get_ratios_of_column("age", data)
    print(ratios[2])
    country_list = list_of_countries(data)
    parser = argparse.ArgumentParser(usage = usage_statement(data))
    parser.add_argument("--function", type = str, help = "Usage: python3 ProductionCode/cl_code.py --function <function_name> \
                        --country <country_name>\nFunction options:\ninternet_access_by_country, average_age_of_country") 
    parser.add_argument("--country", type = str, help = "Country options:\nHint: If the country is multiple words long, \
                        enclose the name in quotes.\n" + string_of_countries(country_list))
    arguments = parser.parse_args()

    if arguments.function == "internet_access_by_country":
        percentage_internet_access_by_country = percentage_with_internet_access(arguments.country, data)
        internet_result = str(percentage_internet_access_by_country) + " percent of " + arguments.country + " has internet access."
        print(internet_result)
    
    elif arguments.function == "average_age_of_country":
        average_age_of_country = get_average_of_column(arguments.country, "age", data)
        age_result = str(average_age_of_country) + " is the average age of people in " + arguments.country + "."
        print(age_result)

    
if __name__ == "__main__":
    main()



    
    
    
