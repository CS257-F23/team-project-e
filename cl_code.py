import csv
import argparse
from ProductionCode.core import *
    
def argument_parser():
    """ Returns the argument that is inputed into the terminal by the user
        input: list [data] 
        output: string (arguments)"""
    dataset = Dataset()
    parser = argparse.ArgumentParser(usage = dataset.usage_statement())
    parser.add_argument("--function", type = str, help = "Usage: python3 ProductionCode/cl_code.py --function <function_name> \
                        --country <country_name>\nFunction options:\nfour_stat_summary, financial_account_comparison, age_education_worry_comparison") 
    parser.add_argument("--country", type = str, help = "Country options:\nHint: If the country is multiple words long, \
                        enclose the name in quotes.\n" + dataset.string_of_countries())
    arguments = parser.parse_args()

    return arguments

def function_argument_choice(arguments):
    """ Returns the data result associated with the specifc argument the user types into the terminal.
    input: arguments(string), list[data]
    output: four_main_stats_of_interest(string) , or financial_comparison_results (string), or age_education_results (string), or usage statement(string)
    """
    dataset = Dataset()
    dataset.load_data()

    if arguments.function == "four_stat_summary":
        four_main_stats_of_interest = dataset.four_stat_summary_by_country(arguments.country)
        return four_main_stats_of_interest
    
    elif arguments.function == "financial_account_comparison":
        financial_account_by_country = dataset.has_financial_account_single_country(arguments.country)
        financial_account_global = dataset.has_financial_account_global()
        financial_comparison_results = dataset.format_financial_comparison(arguments.country, financial_account_by_country, financial_account_global)
        return financial_comparison_results
        
    elif arguments.function == "age_education_worry_comparison":
        age_education_results = dataset.format_age_financial_worry_by_education_summary(arguments.country)
        return age_education_results

    else:
        usage_statement_message = dataset.usage_statement()
        return usage_statement_message



def main():
    """Loads the data, parses the command line, and prints the results of the specificed command line function.
    Output: the data associated with the argument associated with the command line"""

    dataset = Dataset()
    data = dataset.load_data()
        
    arguments = argument_parser()

    country_validity = dataset.check_keyword_validity(arguments.country, "economy")

    if country_validity == True:

        print(function_argument_choice(arguments))
        
    else:
        usage_statement_message = dataset.usage_statement()
        print(usage_statement_message)

        
if __name__ == "__main__":
    main()




    
    
    
