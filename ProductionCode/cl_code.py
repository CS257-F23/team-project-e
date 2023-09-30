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

def percentage_with_internet_access(country):
    """Takes a country and returns a number representing the 
    percentage of people from that country with internet access"""
    
    return

    
    
    
