import sys
import csv

def load_data():
    """Loads the data and returns it as a list"""
    
    rows = []
    
    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            rows.append(row)
            
    return rows    

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
    
    has_internet_access = "1"
    
    country_data = filter(country, "economy", data)
    
    internet_column = get_column("internetaccess", country_data)
    
    percentage = get_ratio(has_internet_access, internet_column) * 100
    
    return round(percentage, 1)

def get_ratio(key, column):
    
    num = column.count(key)
    total = len(column)
    
    ratio = num / total
    
    return ratio

def get_ratios(column):
    ratios = []
    
    for item in set(column):
        ratio = get_ratio(item, column)
        ratios.append(ratio)
        
    return ratios

def education_level_by_gender(country, data):
    
    country_data = filter(country, "economycode", data)
    
    educ_column = get_column("educ", country_data)
    
    ratios = get_ratios(educ_column)
    
    return ratios
    
    

def main():
    """Loads in the dataset and calls the command line functions."""
    data = load_data()
    country = sys.argv[1]
    percentage_internet_access_by_country = percentage_with_internet_access(country, data)
    print(str(percentage_internet_access_by_country) + " percent of " + str(country) + " has internet access.")

main()



    
    
    
