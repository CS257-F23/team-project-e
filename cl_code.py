import argparse
from ProductionCode.core import *
    
def argument_parser():
    """Returns the argument that is inputed into the terminal by the user.
    Input: None 
    Returns: command line arguments (string)"""
    parser = argparse.ArgumentParser(usage = data.get_usage_statement())
    parser.add_argument("--function", type = str, help = "Usage: python3 ProductionCode/cl_code.py --function <function_name> \
                        --country <country_name>\nFunction options:\nfour_stat_summary, financial_account_comparison, age_education_worry_comparison") 
    parser.add_argument("--country", type = str, help = "Country options:\nHint: If the country is multiple words long, \
                        enclose the name in quotes.\n" + data.get_string_of_countries())
    arguments = parser.parse_args()

    return arguments

def get_function_results(arguments):
    """ Returns the result associated with the specific function argument the user types into 
    the terminal. If the function is not valid, the usage message is returned.
    Input: command line arguments (string)
    Returns: results associated with the given function (string)
    or the usage statement (string)
    """
    if arguments.function == "four_stat_summary":
        four_main_stats_of_interest = data.get_formatted_four_stat_summary_by_country(arguments.country)
        return four_main_stats_of_interest
    
    elif arguments.function == "financial_account_comparison":
        financial_comparison_results = data.get_formatted_financial_comparison(arguments.country)
        return financial_comparison_results
        
    elif arguments.function == "age_education_worry_comparison":
        age_education_results = data.get_formatted_age_financial_worry_by_education_summary(arguments.country)
        return age_education_results

    else:
        usage_statement_message = data.get_usage_statement()
        return usage_statement_message
    
def get_results_if_valid_country(arguments):
    """Calls get_function_results if the user enters a valid country.
    If the country is not valid, the usage message is returned. 
    Input: command line arguments (string)
    Returns: results associated with the given country (string)
    or the usage statement (string)
    """
    if data.get_country_validity(arguments.country):
        results = get_function_results(arguments)
        return results
    else:
        usage_statement_message = data.get_usage_statement()
        return usage_statement_message

def has_function_argument(arguments):
    """Checks that the user provided a function argument through
    the command line.
    Input: command line arguments (string)
    Returns: if a function argument was given or not (boolean)
    """
    function_argument = True
    if arguments.function == None:
        function_argument = False
    return function_argument

def has_country_argument(arguments):
    """Checks that the user provided a country argument through
    the command line.
    Input: command line arguments (string)
    Returns: if a country argument was given or not (boolean)
    """
    country_argument = True
    if arguments.country == None:
        country_argument = False
    return country_argument
            
def main():
    """Loads the data, parses the command line, and prints the results of the specificed command line function.
    Input: None
    Returns: the results associated with the given arguments (string)"""    
    arguments = argument_parser()

    if has_function_argument(arguments) and has_country_argument(arguments):
            print(get_results_if_valid_country(arguments))
    else:
        usage_statement_message = data.get_usage_statement()
        print(usage_statement_message)

        
if __name__ == "__main__":
    data = Dataset()
    data.connect()
    main()




    
    
    
