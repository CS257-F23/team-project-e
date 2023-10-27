import unittest
import subprocess
from app import *

class test_flask_app(unittest.TestCase):
    def test_route_homepage(self):
        """ This function tests the route of the homepage and if the words presented on the homepage are correct """
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects = True)

        word = "Welcome"
        page = str(response.data)
        
        self.assertIn(word, page)

    def test_route_internet_access(self):
        """ This function tests the route for the page that shows the internet access data and correctly returns the percent of people with interenet access.  """
        self.app = app.test_client()
        response = self.app.get('/four_stat_summary/Panama', follow_redirects = True)
        
        item = "58.5"
        page = str(response.data)

        self.assertIn(item, page)

    def test_route_average_age(self):
        """This function tests the route for the page that shows the route that shows the average age of a country and correctly returns the average age."""
        self.app = app.test_client()
        response = self.app.get('/four_stat_summary/Norway', follow_redirects = True)
        
        item = "Norway"
        page = str(response.data)

        self.assertIn(item, page)

    def test_route_error_handler(self): 
        """" Function tests the route of the error handler and correctly returns the response."""
        self.app = app.test_client()
        response = self.app.get('404', follow_redirects = True)
        
        self.assertEqual(b'must', response.data[4:8])

    def test_incorrect_country_name(self):
        """Test function for when there is an incorect country name input"""
        self.app = app.test_client()
        response = self.app.get('/four_stat_summary/Canad', follow_redirects = True)
        
        self.assertIn(b'Server Error', response.data)

    def test_not_enough_argvs(self):
        """Test function for when there are not enough argumnets in the input"""
        self.app = app.test_client()
        response = self.app.get('/four_stat_summary', follow_redirects = True)
        self.assertIn(b'wrong route', response.data)


    def test_incorrect_function_name(self):
        """Test function for when there is an incorrect function name inputed"""
        self.app = app.test_client()
        response = self.app.get('/fourstatsummary/Argentina', follow_redirects = True)
        self.assertIn(b'wrong route', response.data)

    def test_too_many_inputs(self):
        """Test function for when there are too many inputs"""
        self.app = app.test_client()
        response = self.app.get('/four_stat_summary/Argentina/Costa Rica', follow_redirects = True)
        self.assertIn(b'wrong route', response.data)


if __name__ == '__main__':
    unittest.main()