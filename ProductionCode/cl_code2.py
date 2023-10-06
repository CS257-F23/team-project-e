import sys
import csv

"""USAGE STATEMENTS:
python3 ProductionCode/cl_code.py --internet_access_by_country country_name
python3 ProductionCode/cl_code.py --education_levels_by_country_and_gender country_name"""

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

def check_country_validity(country, data):
    """Checks if the country that the user entered is in the dataset or if it is an invalid country"""
    is_country_in_data = False
    idx = get_column_index("economy")
    
    for row in data:
        
        if row[idx] == country:
            is_country_in_data = True

    return is_country_in_data

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
    
    country_validty = check_country_validity(country, data)

    if country_validty == False:
        return "Please enter a valid country. Hint: if the country is multiple words, enclose it in quotes."
    
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



def education_level_by_gender(country, data):
    """Given a country and data, returns the education levels 
    """
    country_validty = check_country_validity(country, data)

    if country_validty == False:
        return "Please enter a valid country. Hint: if the country is multiple words, enclose it in quotes."
    
    country_data = filter(country, "economy", data)
    
    female_data = filter("1", "female", country_data)
    female_educ = get_column("educ", female_data)
    
    male_data = filter("2", "female", country_data)
    male_educ = get_column("educ", male_data)
    
    female_ratios = get_ratios(female_educ)
    male_ratios = get_ratios(male_educ)
    
    ratios = [female_ratios, male_ratios]
    
    return ratios 

def print_education_results(ratios, country):
    """Formats and prints the results of the education_level_by_gender function"""
    female_primary = ratios[0][0][1]
    female_secondary = ratios[0][1][1]
    female_tertiary = ratios[0][2][1]
    male_primary = ratios[1][0][1]
    male_secondary = ratios[1][1][1]
    male_tertiary = ratios[1][2][1]
    print("Education levels in " + country + ":" + "\nFor females:" + "\nPrimary school or less: " + str(female_primary) + " percent"
              + "\nSecondary school: " + str(female_secondary) + " percent" + "\nTertiary education or more: " + str(female_tertiary)
              + " percent" + "\nFor males:" + "\nPrimary school or less: " + str(male_primary) + " percent"
              + "\nSecondary school: " + str(male_secondary) + " percent" + "\nTertiary education or more: " + str(male_tertiary)
              + " percent")
    
def parse_arguments(data):
    """Stores the command line arguments in appropriate variables and returns them"""
    function_tag = sys.argv[1]
    country_name = sys.argv[2]

    return function_tag, country_name

def main():
    """Loads the data, parses the command line, and prints the results of the specified command line function"""
    data = load_data()
    arguments = parse_arguments(data)
    tag = arguments[0]
    country = arguments[1]

    if tag == "--internet_access_by_country":
        percentage_internet_access_by_country = percentage_with_internet_access(country, data)
        print(str(percentage_internet_access_by_country) + " percent of " + country + " has internet access.")

    elif tag == "--education_levels_by_country_and_gender": 
        education_levels_by_country_and_gender = education_level_by_gender(country, data)
        print_education_results(education_levels_by_country_and_gender, country)
    
if __name__ == "__main__":
    main()



    
    
    
