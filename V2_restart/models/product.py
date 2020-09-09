"""
This module will be responsible for the Product objet
It will handle the addition of selected products to the database
"""
import json

class Product:
    """
    This class is responsible for the addition of products to the database
    after an API GET Request to the Open Food Facts API
    """

    def __init__(self):
        self.product_name = " "
        self.category_name = " "
        self.category_id = " "
        self.nutrition_grade = " "
        self.product_desc = " "
        self.product_url = " "
        self.favorite = False
        self.substitute_id = " "

    def add_product(self,product_name,category_name,
                    category_id, nutrition_grade,
                    product_desc, product_url,
                    favorite, substitute_id):
        """Adds the product to the DDB"""

        self.product_name = product_name
        self.category_name = category_name
        self.category_id = category_id
        self.nutrition_grade = nutrition_grade
        self.product_desc = product_desc
        self.product_url = product_url
        self.favorite = favorite
        self.substitute_id = substitute_id
    
    