"""
This module will be responsible for handling the GET requests to the
Open Food Facts API https://documenter.getpostman.com/view/8470508/SVtN3Wzy#intro
"""

import requests
import mysql.connector as mysql
# from classes.category import Category

def read_request():
    """
    Performs a GET request to the OFF API in order to get
    only the categories with more than 15k products
    """
    api_base_url = "https://fr.openfoodfacts.org/categories.json"
    headers = {'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Pur Beurre - Open Class Rooms - V1'}
    response = requests.get(api_base_url, headers=headers)
    data_set = response.json()
    product_nbr = 15000

    # Test looping on categories names of the json response
    # from the API to only get Categories with more than 15k products
    for category in data_set['tags']:
        products = category.get('products')
        if int(products) > product_nbr:
            print("Catégorie : " + category.get('name')
                + " contenant : "
                + str(category.get('products')) + " produits.")
            # for product in products:
            #     pass


# for data in data_set:
#     url = data.get('url')
#     print(url)

print(read_request())



    