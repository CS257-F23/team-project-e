import csv
import argparse
from ProductionCode.core import *



def function_argument_choice(arguments, data):
    """ Returns the data result associated with the specifc argument the user types into the terminal.
    input: arguments(string), list[data]
    output: four_main_stats_of_interest(string) , or financial_comparison_results (string), or age_education_results (string), or usage statement(string)
    """
    if arguments.function == "four_stat_summary":
        four_main_stats_of_interest = four_stat_summary_by_country(arguments.country, data)
        return four_main_stats_of_interest
    
    elif arguments.function == "financial_account_comparison":
        financial_account_by_country = has_financial_account_single_country(arguments.country, data)
        financial_account_global = has_financial_account_global(data)
        financial_comparison_results = format_financial_comparison(arguments.country, financial_account_by_country, financial_account_global)
        return financial_comparison_results
        
    elif arguments.function == "age_education_worry_comparison":
        age_education_results = format_age_financial_worry_by_education_summary(arguments.country, data)
        return age_education_results

    else:
        usage_statement_message = usage_statement(data)
        return usage_statement_message


def main():
    """Loads the data, parses the command line, and prints the results of the specificed command line function.
    Output: the data associated with the argument associated with the command line"""

    data = load_data()
    
    arguments = argument_parser(data)

    country_validity = check_keyword_validity(arguments.country, "economy", data)

    if country_validity == True:

        print(function_argument_choice(arguments, data))
    
    else:
        usage_statement_message = usage_statement(data)
        print(usage_statement_message)

    
if __name__ == "__main__":
    main()



    
    
    
