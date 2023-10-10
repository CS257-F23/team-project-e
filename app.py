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
    
    return str(percentage) + " percent of people have access to the internet from " + country

@app.route("/average_age/<country>")
def age_of_country(country):
    """Returns the average age of people from the given country"""
    
    return "some age"

@app.errorhandler(404)
def page_not_found(e):
    
    return "Wrong page"

if __name__ == "__main__":
    app.run()

