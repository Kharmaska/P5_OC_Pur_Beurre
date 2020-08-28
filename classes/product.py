"""
This module will be responsible for the Product objet
It will handle the addition of selected products to the database
"""

class Product:
    """
    This class is responsible for the addition of products to the database
    after an API GET Request to the Open Food Facts API
    """

    def __init__(self):
        self.product_name = " "
        self.category_name = " "
        self.nutrition_grade = " "
        self.product_url = " "
        self.product_store = " "

    def add_product(self,product_name,category_name,nutrition_grade,product_store,product_url):
        """Adds the product to the DDB"""

        self.product_name = product_name
        self.category_name = category_name
        self.nutrition_grade = nutrition_grade
        self.product_url = product_url
        self.product_store = product_store


    def display_product(self):
        """ Displays the selected product to the user"""
        print(
            "Vous avez sélectionné {} de la catégorie {} \n"
            "Son nutriscore est de rang {} \n"
            "Url du produit : {} \n"
            "Où l'acheter : {}".format(
                self.product_name, self.category_name, self.nutrition_grade,
                self.product_url, self.product_store
            )
        )

#  TO BE REMOVED | Just a fake product for now to test if class instanciation would look correct
newProduct = Product()
newProduct.add_product('Coucou Cola','Boissons','E','Carrouf','sugarfull.org')
newProduct.display_product()
