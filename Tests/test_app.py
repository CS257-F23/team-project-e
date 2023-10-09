
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
        response = self.app.get('internet_access/Panama', follow_redirects = True)
        self.assertEqual(b'58.5 percent of people have access to the internet from Panama', response.data)

     def test_route_average_age(self):
       """This function tests the route for the page that shows the route that shows the average age of a country and correctly returns the average age."""
        self.app = app.test_client()
        response = self.app.get('average_age/Norway', follow_redirects = True)
        self.assertEqual(b'48.5 is the avarage age in Norway', response.data)
# add tests for edge cases and error function
if __name__ == '__main__':
    unittest.main()