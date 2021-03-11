import unittest
import requests


class TestGetApiData(unittest.TestCase):

    def test_api_response_status(self):
        response = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/units")
        assert response.status_code == 200

    def test_if_api_content_type_equals_json(self):
        response = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/units")
        assert response.headers["Content-Type"] == "application/json"

    def test_if_the_first_key_of_response_is_units(self):
        response = requests.get("https://age-of-empires-2-api.herokuapp.com/api/v1/units").json()
        assert list(response.keys())[0] == "units"




