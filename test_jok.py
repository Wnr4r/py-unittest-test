import unittest

from jok import len_joke, get_joke
from unittest.mock import patch, MagicMock

class TestJoke(unittest.TestCase):

    @patch('jok.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "One"
        self.assertEqual(len_joke(), 3)

    @patch('jok.requests')
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': {'joke': 'Not funny'}}
        mock_requests.get.return_value = mock_response #the get object returns an instance of response, due to this we need to mock response as done above

        self.assertEquals(get_joke(), "Not funny")

    @patch('jok.requests')
    def test_failed_get_joke(self, mock_requests):

        mock_response = MagicMock(status_code=500)
        mock_response.json.return_value = {'value': {'joke': 'Not funny'}}
        mock_requests.get.return_value = mock_response #the get object returns an instance of response, due to this we need to mock response as done above

        self.assertEquals(get_joke(), "No Joke")

if __name__ == '__main__':
    unittest.main()
