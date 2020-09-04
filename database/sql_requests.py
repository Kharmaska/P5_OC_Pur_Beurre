"""
Module responsible for SQL PREPARED QUERIES and Login information.
This is where you want to replace the USER | DATABASE & PASSWORD information by yours
"""

# login information to be replaced by user's DB login

USER = 'Miam'
DATABASE = "DBOpenFF"
PASSWORD = 'LeGrasCestLaVie'
HOST = "localhost"
FILE = "dbOpenFoodFacts.sql"

"""MYSQL queries"""

# CREATE Queries

ADD_PRODUCT_DATA = (
    'INSERT INTO Product'
    '(product_name, category_name,nutrition_grade)'
    'VALUES (%s, %s, %s)'
)

ADD_CATEGORY_DATA = (
    'INSERT INTO Category'
    '(category_name)'
    'VALUES (%s)'
)

ADD_SUB_DATA = (
    """INSERT INTO Substitute
    (saved_product_name, saved_product_grade,
    saved_substitute_id, saved_substitute_name,
    saved_substitute_grade, saved_substitute_url,
    saved_substitute_store)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """)

# READ Queries

DISPLAY_CATEGORIES = ("SELECT id, category_name from Category")

DISPLAY_A_CATEGORY = (
    "SELECT Product.id, Product.product_name from Product"
    "INNER JOIN Category"
    "ON Product.category_name = Category.category_name"
    "WHERE Category.id = %s"
)

DISPLAY_SUBSTITUTE = (
    """SELECT saved_product_id, saved_product_name as replaced_product,
    saved_product_grade, saved_substitute_id , saved_substitute_name,
    saved_substitute_grade , saved_substitute_url , saved_substitute_store
    FROM substitute
    """)

# UPDATE Queries

UPDATE_PRODUCT_DATA = (
    "UPDATE PRODUCT"
    "INNER JOIN Category ON Category.category_name = Product.category_name"
    "SET Product.category_id = Category.id"
    "WHERE Product.category_name = category.category_name"
)



