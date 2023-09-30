import sys
import csv

def load_data():
    """Loads the data and returns it as a list"""
    
    rows = []
    
    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
            
    return rows

def load_header():
    """Loads the column names and returns them as a list"""

    with open('Data/world_bank.csv', "r") as file:
        reader = csv.reader(file)
        column_names = next(reader)

    return column_names

def group_by_country(country): 
    country_list = []
    for row in data:
        if row[0] == country:
            country_list.append(row)
    return country_list
def group_by_internet_access(country_list): 
    internet_list = []
    column_names = load_header()
    col = column_names.index("internetaccess")
    for row in country_list:
        internet_list.append(row[col])
    return internet_list
def percentage_with_internet_access(country):
    yes_internet_access = "1"
    country_list = group_by_country(country)
    internet_list = group_by_internet_access(country_list)
    percentage = (internet_list.count(yes_internet_access)/len(internet_list)) * 100
    return percentage

#put the sys argv stuff in a main function
country = sys.argv[1]
data = load_data()
print(percentage_with_internet_access(country))


print(load_data())

    
    
    
