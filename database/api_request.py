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
data_set = response.json()

# Test looping on categories names of the json response
# from the API to only get Categories with more than 15k products
for data in data_set['tags']:
    if int(data.get('products')) > 15000:
        print("Catégorie : " + data.get('name')
               + " contenant : "
               + str(data.get('products')) + " produits.")

# for data in data_set:
#     url = data.get('url')
#     print(url)
    