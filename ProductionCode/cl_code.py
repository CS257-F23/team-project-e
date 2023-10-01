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
    
    num = internet_column.count(has_internet_access)
    total = len(internet_column)
    
    percentage = (num / total) * 100
    
    return percentage

def main():
    #put the sys argv stuff in a main function
    #country = sys.argv[1]
    
    data = load_data()
    print(percentage_with_internet_access("United States", data))

main()


#print(load_data())

    
    
    
