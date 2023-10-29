# Import what we need for testing
import unittest
from main import app

class TestApp(unittest.TestCase):
    
    def test_index(self):
        # Create a test client using the Flask app context
        with app.test_client() as client:
            # Make a GET request to the index route
            response = client.get('/')
            # Check that the response status code is 200 OK
            self.assertEqual(response.status_code, 200)
    
    def test_cow(self):
        # Create a test client using the Flask app context
        with app.test_client() as client:
            # Make a GET request to the cow route
            response = client.get('/cow')
            # Check that the response status code is 200 OK
            self.assertEqual(response.status_code, 200)
            # Check that the response data is the expected string
            self.assertEqual(response.data.decode('utf-8'), 'MOoooOo!')
