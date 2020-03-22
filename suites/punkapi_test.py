import os
import sys
import unittest

api_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),os.path.join("src","api"))
print(api_path)
sys.path.append(api_path)

from http_api import http_api

app = http_api("https://api.punkapi.com/v2/")

class punkapi_test(unittest.TestCase):


    def test_beer_app(self):
        resp = app.get_response("get", "beers?page=1&per_page=80")

        with open("beer_page_1_80.exp") as f:
            expectation = f.read()

        self.assertEqual(expectation, resp.content)
        

    def test_beer_app_search(self):
        resp = app.get_response("get", "beers?beer_name=buzz&page=1&per_page=80")

        with open("beer_name_page_1_80.exp") as f:
            expectation = f.read()

        self.assertEqual(expectation, resp.content)
