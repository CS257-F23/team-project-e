import sys
import csv

"""USAGE STATEMENTS:
python3 ProductionCode/cl_code.py --internet_access_by_country country_name
python3 ProductionCode/cl_code.py --education_levels_by_country_and_gender country_name"""


def load_data():
    """Loads the data and returns it as a list"""
    
    global data
    global header
    
    data = []
    header = {}
    
    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
        column_names = next(reader)
        
        for i, name in enumerate(column_names):
            header[name] = i
            
        for row in reader:
            data.append(row)
            
    #return data  

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
    """Takes a country name, a column name, and the dataset, and returns
    the average of the values in the column"""

    check_country_validity(country, data)

    country_data = filter(country, column, data)
    avg = calculate_average(country_data)
    
    return avg

def calculate_average(column):
    """Takes a list of numerical values, and returns the mean of the list"""
    total = sum(column)
    length = len(column)

    avg = total / length

    return avg
    
def parse_arguments():
    """Stores the command line arguments in appropriate variables and returns them"""
    function_tag = sys.argv[1]
    country_name = sys.argv[2]

    return function_tag, country_name

def main():
    """Loads the data, parses the command line, and prints the results of the specified command line function"""
    load_data()
    arguments = parse_arguments()
    tag = arguments[0]
    country = arguments[1]

    if tag == "--internet_access_by_country":
        percentage_internet_access_by_country = percentage_with_internet_access(country, data)
        print(str(percentage_internet_access_by_country) + " percent of " + country + " has internet access.")

    elif tag == "-- average_age_of_country": 
        average_age = get_average_of_column(country, "age", data) 
    
if __name__ == "__main__":
    main()



    
    
    
