"""
This module will be responsible for the Substitute objet
It will handle saving substitution items with a better nutrition grade
than selected products in the database
"""

class Substitute:
    """
    This class is responsible for the addition of products to the database
    after an API GET Request to the Open Food Facts API
    """

    def __init__(self):
        self.substitute_name = " "
        self.category_name = " "
        self.substitute_grade = " "
        self.substitute_url = " "
        self.substitute_store = " "
        self.substitute_id = 0
        self.origin_product = 0

    def add_substitute(self,substitute_name,category_name,substitute_grade,
                       substitute_store,substitute_url, substitute_id, origin_product):
        """Adds the substitution product to the DDB"""

        self.substitute_name = substitute_name
        self.category_name = category_name
        self.substitute_grade = substitute_grade
        self.substitute_url = substitute_url
        self.substitute_store = substitute_store
        self.substitute_id = substitute_id
        self.origin_product = origin_product


    def display_substitute(self):
        """ Displays the selected substitution product to the user"""
        print(
            "Vous avez sélectionné {} de la catégorie {} \n"
            "En remplacement de {} \n"
            "Son nutriscore est de rang {} \n"
            "Url du produit : {} \n"
            "Où l'acheter : {}".format(
                self.substitute_name, self.category_name, self.origin_product,
                self.substitute_grade,
                self.substitute_url, self.substitute_store
            )
        )

#  TO BE REMOVED | Just a fake product for now to test if class instanciation would look correct
newSubstitute = Substitute()
newSubstitute.add_substitute('Better Cola','Boissons','C',
                             'BioTop','sugarfull.org',12, 'Coucou Cola')
newSubstitute.display_substitute()
