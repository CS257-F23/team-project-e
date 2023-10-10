
import unittest
import subprocess
from app import *

class test_flask_app(unittest.TestCase):
    def test_route_homepage(self):
        """ This function tests the route of the homepage and if the words presented on the homepage are correct """
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(b"There are 2 functions for this app. 1. You can type in internet_access/[insert country here], and get the p", response.data)

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