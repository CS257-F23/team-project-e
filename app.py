from flask import Flask
from ProductionCode.cl_code2 import * #CHANGE TO cl_code BEFORE TURNING IN

app = Flask(__name__)

data = load_data()

@app.route("/")
def homepage():
    """The homepage of our app"""
    
    country_list = list_of_countries(data)
    
    countries_string = string_of_countries(country_list)

    home_page_message = "Welcome to our World Bank Financial Data Website! <br><br> \
        There are 2 functionalities for this app. You can either find the percentage \
        of people in a certain country that have internet access, or you can find the average age of \
        people in a given country. <br><br> The list of countries that you can choose from is: <br><br> " + countries_string + " <br><br> To run \
        the internet access function, type /internet_access/[country_name] after the URL. <br> To run the age function, type \
        /average_age/[country_name] after the URL. "
    
    return home_page_message


@app.route("/internet_access/<country>")
def internet_access_of_country(country):
    """Returns the percentage of people with access to the internet
    from the given country"""
    
    percentage = percentage_with_internet_access(country, data)
    
    return str(percentage) + " percent of people from " + country + " have access to the internet."

@app.route("/average_age/<country>")
def age_of_country(country):
    """Returns the average age of people from the given country"""
    
    age = get_average_of_column(country, "age", data)
    
    return "The average age of people in " + country + " is " + str(age) + "."

@app.errorhandler(404)
def page_not_found(e):
    
    return """You must have typed in the wrong route. Remember, to use this website, either: <br>
    1. Type in /average_age/[country name], e.g: /average_age/Nigeria <br>
    2. Type in /internet_access/[country name], e.g: /internet_access/Mexico"""

if __name__ == "__main__":
    app.run()

