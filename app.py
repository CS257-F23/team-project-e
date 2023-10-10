from flask import Flask
from ProductionCode.cl_code2 import * #CHANGE TO cl_code BEFORE TURNING IN

app = Flask(__name__)

data = load_data()

@app.route("/")
def homepage():
    """The homepage of our app"""
    
    country_list = list_of_countries(data)
    
    countries_string = string_of_countries(country_list)

    home_page_message = "There are 2 functionalities for this app. You can either find the percentage \
        of people in a certain country that have internet access, or you can find the average age of \
            people in a given country. The list of countries that you can choose from is: " + countries_string
    
    return '''There are 2 functions for this app.

1. You can type in internet_access/[insert country here], and get
the p'''

@app.route("internet_access/<country>")
def internet_access_of_country(country):
    """Returns the percentage of people with access to the internet
    from the given country"""
    
    percentage = percentage_with_internet_access(country, data)
    
    return str(percentage) + " percent of people have access to the internet from " + country

@app.route("average_age/<country>")
def age_of_country(country):
    """Returns the average age of people from the given country"""
    
    return "some age"

@app.errorhandler(404)
def page_not_found(e):
    
    return "Wrong page"

