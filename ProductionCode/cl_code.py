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


def percentage_with_internet_access(country):
    # deal with 3 and 4 values of internet access
    """Takes a country and returns a number representing the 
    percentage of people from that country with internet access"""
    country_list = []
    internet_list = []
    column_names = load_header()
    col = column_names.index("internetaccess")
    for row in data:
        # group by country
        if row[0] == country:
            country_list.append(row)
    for row in country_list:
        internet_list.append(row[col])
    return (internet_list.count("1")/len(internet_list)) * 100
#put the sys argv stuff in a main function
country = sys.argv[1]
data = load_data()
print(percentage_with_internet_access(country))
    

    
    
    
