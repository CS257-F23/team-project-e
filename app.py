from flask import Flask , render_template, request
from ProductionCode.core import * 

app = Flask(__name__)

data = Dataset()
data.load_data()

@app.route("/")
def homepage():
    """This is the homepage of our app. This route takes in no parameters and
    returns the message that is printed to the home page."""
    
    countries_string = data.string_of_countries()
    function_name = ['summary of four interesting statistics', 'financial account summary', 'age and educaiton comparison']
    """
    home_page_message = "Welcome to our World Bank Financial Data Website! <br><br> \
        There are 3 functionalities for this app. You can either retrieve a summary of four interesting \
        statistics about a country, compare the percentage of a country that has a financial account to the \
        worldwide statistic, or compare the average age of a country to the percentage of the population that is \
        worried about financing their education. <br><br> The list of countries that you can choose from is: \
        <br><br> "  + countries_string + " <br><br> To run the four statistics summary, type /four_stat_summary/[country_name] \
        after the URL. <br> To run the financial account comparison function, type financial_account_comparison/[country_name] \
        after the URL. <br> To run the age and worry about financing education comparison function, \
        type /age_education_comparison/[country_name] after the URL. <br><br>You can use these statistics about various countries \
        to learn about the financial and demographic status of a given country. By providing the comparison of these statistics across \
        multiple countries globally, we provide invaluable data for researchers, professors, and students alike."
    """
    return render_template('homepage.html',countries = countries_string, functions = function_name, countriesValue = data.list_of_countries())


#this is to display the data from the form ?? mostly likely wrong code
"""@app.route('/datastatistics') # I think we need to turn in our flask revisions before we add this stuff into this file
bc the flask assignment doesn't use html
def display_out_data():
    output = str(request.args['specficData'])
    
    return render_template('dataStatsPage.html', the_data = output)

@app.route('/dataPage')
def statement_about_our_data():
    return render_template('dataPage.html', about = "World Bank Financial Data")
"""

@app.route("/four_stat_summary/<country>")
def get_four_stat_summary(country): 
    """This route returns a summary of four interesting statistics 
    about the given country. It takes a country as a route parameter 
    and returns a message containing the statistics. """
    
    summary = data.four_stat_summary_by_country(country)

    population = summary[0]
    internet = summary[1]
    education = summary[2]
    employment = summary[3]

    message = "Population of " + country + ": " + str(population) + "<br>Percentage of " + country + " that has internet access: " + str(internet) + "<br>Percentage of " + country + " that has attained tertiary education or higher: " + str(education) + "<br>Percentage of " + country + " that is employed: " + str(employment)

    return message

@app.route("/financial_account_comparison/<country>")
def get_financial_account_comparison(country): 
    """This route returns a comparison of the percentage of the given
    country that has a financial account versus the global statistic. 
    It takes a country as a route parameter and returns a message 
    containing the comparison statistics."""
    
    country_result = data.has_financial_account_single_country(country)
    global_result = data.has_financial_account_global()

    message = "Percentage of people in " + country + " who have a financial account: " + str(country_result) + "<br>Percentage of people worldwide who have a financial account: " + str(global_result)
    
    return message

@app.route("/age_education_comparison/<country>")
def get_age_education_comparsion(country):
    """This route returns a comparison of the average age of a country and 
    the percentage of a country that is worried about financing their education. 
    It takes a country as a route parameters and returns a message containing
    the comparison statistics."""

    average_age = data.average_age_by_country(country)
    financial_worry = data.financial_worry_education_by_country(country)

    message = "Average age of " + country + ": " + str(average_age) + "<br>Percentage of people in " + country + " who are worried about financing their education: " + str(financial_worry)

    return message

@app.route("/help")
def helper_page():
    return render_template('helpPage.html')

@app.errorhandler(404)
def page_not_found(e):
    """This route returns the usage statement for all functions if 
    the page cannot be found. It doesn't take any parameters and returns 
    a help statement for the user."""

    error_message = """You must have typed in the wrong route. Remember, to use this website, either: <br>
    1. Type in /four_stat_summary/[country name], e.g: /four_stat_summary/Nigeria <br>
    2. Type in /financial_account_comparison/[country name], e.g: /financial_account_comparison/Mexico <br>
    3. Type in /age_education_comparison/[country_name], e.g: /age_education_comparison/Malawi"""
    
    return error_message

if __name__ == "__main__":
    app.run()

