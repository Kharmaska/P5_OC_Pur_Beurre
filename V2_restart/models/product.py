"""
This module will be responsible for the Product objet
It will handle the addition of selected products to the database
"""

import mysql.connector
from database.sql_requests import *

class Product:
    """
    This class is responsible for the addition of products to the database
    after an API GET Request to the Open Food Facts API
    """

    def __init__(self):
        self.product_name = " "
        self.category_name = " "
        self.nutrition_grade = " "
        self.product_id = 0
        my_sql_config = {
            "user": USER,
            "password": PASSWORD,
            "host": HOST,
            "database": DATABASE,
        }
        self.mydb = mysql.connector.connect(**my_sql_config)
        self.cursor = self.mydb.cursor(buffered=True)

    def add_product(self,product_name,category_name,
                    nutrition_grade, product_id):
        """Adds the product to the DDB"""

        self.product_name = product_name
        self.category_name = category_name
        self.nutrition_grade = nutrition_grade
        self.product_id = product_id
        
        add_prod = (
            self.product_name,
            self.category_name,
            self.nutrition_grade,
            self.product_id
        )
        
        try:
            self.cursor.execute(ADD_PRODUCT_DATA, add_prod)
            self.cursor.execute(UPDATE_PRODUCT_DATA)
            self.mydb.commit()
        
        except mysql.connector.errors.IntegrityError:
            pass
    
    def cursor_closed(self):
        self.cursor.close()
        self.mydb.close()

    def display_product(self):
        """ Displays the selected product to the user"""
        print(
            "Vous avez sélectionné {} de la catégorie {} \n"
            "Son nutriscore est de rang {} \n".format(
                self.product_name,
                self.category_name,
                self.nutrition_grade
                )
        )

    def save_substitute(self):
        """ Saves the selected substitute to the user's database"""

        # TBD
        pass

#  TO BE REMOVED | Just a fake product for now to test if class instanciation would look correct
newProduct = Product()
newProduct.add_product('Coucou Cola','Boissons','E',12458)
newProduct.display_product()
