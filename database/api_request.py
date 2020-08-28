"""
This module will be responsible for handling the GET requests to the
Open Food Facts API https://documenter.getpostman.com/view/8470508/SVtN3Wzy#intro
"""

import json
import requests


API_URL_BASE = "https://fr.openfoodfacts.org/categories.json"
headers = {'Content-Type': 'application/json; charset=utf-8',
           'User-Agent': 'Pur Beurre - Open Class Rooms - V1'}


response = requests.get(API_URL_BASE, headers=headers)
print(response)
data = response.json()
print(type(data))
print(data)
