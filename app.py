from flask import Flask, render_template, request
from ProductionCode.core import * 

app = Flask(__name__)

data_set = []
data = Dataset()
data.connect()

@app.route("/")
def homepage():
    """This is the homepage of our app. This route takes in no parameters and
    returns the message that is printed to the home page."""
    
    list_of_countries = data.list_of_countries()
    function_names = ['Summary of four interesting statistics', 'Financial account summary', 'Age and education comparison']
    return render_template('homepage.html', countries = list_of_countries, functions = function_names)

@app.route("/get_function_and_country", methods = ["GET","POST"])
def present_stats():
    function_name = request.form['function_name']
    country = request.form['country_name']
    
    if (function_name == "Summary of four interesting statistics"):
        page = get_four_stat_summary(country)
    elif (function_name == "Financial account summary"):
        page = get_financial_account_comparison(country)
    elif (function_name == "Age and education comparison"):
        page = get_age_education_comparison(country)
        
    return render_template("dataStatsPage.html", webpage = page, heading = function_name)

@app.route('/datastatistics') 
def display_out_data():
    output = str(request.args['specificData'])
    
    return render_template('dataStatsPage.html', the_data = output)

@app.route('/dataPage')
def statement_about_our_data():
    return render_template('dataPage.html', about = "World Bank Financial Data")


@app.route("/four_stat_summary/<country>")
def get_four_stat_summary(country): 
    """This route returns a summary of four interesting statistics 
    about the given country. It takes a country as a route parameter 
    and returns a message containing the statistics. """

    #if data.check_keyword_validity(country, "economy", data_set) == True:
    summary = data.four_stat_summary_by_country(country)

    population = summary[0]
    internet = summary[1]
    education = summary[2]
    employment = summary[3]
    
    first_line = "Population of " + country + ": " + str(population)
    second_line = "Percentage of " + country + " that has internet access: " + str(internet) 
    third_line = "Percentage of " + country + " that has attained tertiary education or higher: " + str(education) 
    fourth_line = "Percentage of " + country + " that is employed: " + str(employment)

    return [first_line, second_line, third_line, fourth_line]

@app.route("/financial_account_comparison/<country>")
def get_financial_account_comparison(country): 
    """This route returns a comparison of the percentage of the given
    country that has a financial account versus the global statistic. 
    It takes a country as a route parameter and returns a message 
    containing the comparison statistics."""
    
    country_result = data.has_financial_account_single_country(country)
    global_result = data.has_financial_account_global()

    first = "Percentage of people in " + country + " who have a financial account: " + str(country_result) 
    second = "Percentage of people worldwide who have a financial account: " + str(global_result)
    
    return [first, second]

@app.route("/age_education_comparison/<country>")
def get_age_education_comparison(country):
    """This route returns a comparison of the average age of a country and 
    the percentage of a country that is worried about financing their education. 
    It takes a country as a route parameters and returns a message containing
    the comparison statistics."""

    average_age = data.average_age_by_country(country)
    financial_worry = data.financial_worry_education_by_country(country)

    first = "Average age of " + country + ": " + str(average_age) 
    second = "Percentage of people in " + country + " who are worried about financing their education: " + str(financial_worry)
    
    return [first, second]

@app.route("/help")
def helper_page():
    return render_template('helpPage.html')

@app.errorhandler(404)
def page_not_found(e):
    """This route returns the usage statement for all functions if 
    the page cannot be found. It doesn't take any parameters and returns 
    a help statement for the user."""

    error_message = """You must have typed in the wrong route. Remember, to use this website, either: <br />
    1. Type in /four_stat_summary/[country name], e.g: /four_stat_summary/Nigeria <br />
    2. Type in /financial_account_comparison/[country name], e.g: /financial_account_comparison/Mexico <br />
    3. Type in /age_education_comparison/[country_name], e.g: /age_education_comparison/Malawi"""
    
    return error_message

if __name__ == "__main__":
    app.run(port = 5204)

