import unittest
import subprocess
from app import *

class test_flask_app(unittest.TestCase):
    def test_route_homepage(self):
        """ This function tests the route of the homepage and if the words presented on the homepage are correct """
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(b"Welcome to our World Bank Financial Data Website! <br><br> \
        There are 2 functionalities for this app. You can either find the percentage \
        of people in a certain country that have internet access, or you can find the average age of \
        people in a given country. <br><br> Afghanistan Albania Algeria Argentina Armenia Australia Austria Azerbaijan Bangladesh Belgium Benin Bolivia Bosnia and Herzegovina Botswana Brazil Bulgaria Burkina Faso Cambodia Cameroon Canada Chad Chile China Colombia Comoros Congo, Dem. Rep. Congo, Rep. Costa Rica Croatia Cyprus Czechia Denmark Dominican Republic Ecuador Egypt, Arab Rep. El Salvador Estonia Eswatini Ethiopia Finland France Gabon Gambia, The Georgia Germany Ghana Greece Guatemala Guinea Honduras Hong Kong SAR, China Hungary Iceland India Indonesia Iran, Islamic Rep. Iraq Ireland Israel Italy Jamaica Japan Jordan Kazakhstan Kenya Korea, Rep. Kosovo Kyrgyz Republic Lao PDR Latvia Lebanon Lesotho Liberia Lithuania Madagascar Malawi Malaysia Mali Malta Mauritania Mauritius Mexico Moldova Mongolia Morocco Mozambique Myanmar Namibia Nepal Netherlands New Zealand Nicaragua Niger Nigeria North Macedonia Norway Pakistan Panama Paraguay Peru Philippines Poland Portugal Romania Russian Federation Saudi Arabia Senegal Serbia Sierra Leone Singapore Slovak Republic Slovenia South Africa South Sudan Spain Sri Lanka Sweden Switzerland Taiwan, China Tajikistan Tanzania Thailand Togo Tunisia Uganda Ukraine United Arab Emirates United Kingdom United States Uruguay Uzbekistan Venezuela, RB Vietnam West Bank and Gaza Yemen, Rep. Zambia Zimbabwe <br><br> To run \
        the internet access function, type /internet_access/[country_name] after the URL. <br> To run the age function, type \
        /average_age/[country_name] after the URL. <br><br> You can use these statistics about various countries to \
learn about the financial and demographic status of a given country. By allowing the use to compare these statistics across \
multiple countries globally, we provide invaluable data for researchers, professors, and students alike.", response.data)

    def test_route_internet_access(self):
        """ This function tests the route for the page that shows the internet access data and correctly returns the percent of people with interenet access.  """
        self.app = app.test_client()
        response = self.app.get('/internet_access/Panama', follow_redirects = True)
        self.assertEqual(b'58.5 percent of people have access to the internet from Panama', response.data)

    def test_route_average_age(self):
        """This function tests the route for the page that shows the route that shows the average age of a country and correctly returns the average age."""
        self.app = app.test_client()
        response = self.app.get('/average_age/Norway', follow_redirects = True)
        self.assertEqual(b'48.5 is the avarage age in Norway', response.data)

    def test_route_error_handler(self): 
        """" Function tests the route of the error handler and correctly returns the response."""
        self.app = app.test_client()
        response = self.app.get('404', follow_redirects = True)
        self.assertEqual(b'Wrong page', response.data)

    def test_incorrect_country_name(self):
        """Test function for when there is an incorect country name input"""
        self.app = app.test_client()
        response = self.app.get('/internet_access/Argentina/Costa Ric', follow_redirects = True)
        

        self.assertEqual(b'p', response.data[0])


    def test_not_enough_argvs(self):
        """Test function for when there are not enough argumnets in the input"""
        self.app = app.test_client()
        response = self.app.get('/internet_access/Argentina', follow_redirects = True)
        self.assertEqual(b'Wrong page', response.data)


    def test_incorrect_function_name(self):
        """Test function for when there is an incorrect function name inputed"""
        self.app = app.test_client()
        response = self.app.get('/internet_acces/Argentina', follow_redirects = True)
        self.assertEqual(b'Wrong page', response.data)

    def test_too_many_inputs(self):
        """Test function for when there are too many inputs"""
        self.app = app.test_client()
        response = self.app.get('/internet_access/Argentina/Costa Rica', follow_redirects = True)
        self.assertEqual(b'You must have typed in the wrong route. Remember, to use this website, either: \
                            1. Type in /average_age/[country name], e.g: /average_age/Nigeria \
                            2. Type in /internet_access/[country name], e.g: /internet_access/Mexico', response.data)


# add tests for edge cases and error function
if __name__ == '__main__':
    unittest.main()