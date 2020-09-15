"""
This module will be responsible for the Category objet
It will handle display of the categories coming from the OFF API
"""

class Category:
    """
    This class is responsible for the addition of products to the database
    after an API GET Request to the Open Food Facts API
    """

    def __init__(self):

        self.category_name = " "
        self.product_number = " "
        self.category_id = 0

    def add_category(self,category_name, product_number):
        """Adds the category to the DDB"""

        self.category_name = category_name
        self.product_number = product_number

    def display_category(self):
        """ Displays the selected category to the user"""
        print(
            "Vous avez sélectionné la catégorie {} \n"
            "Cette dernière contient {} produit(s) \n".format(
                self.category_name, self.product_number)
        )

#  TO BE REMOVED | Just a fake product for now to test if class instanciation would look correct
newCategory= Category()
newCategory.add_category('Boissons', 9000)
newCategory.display_category()
